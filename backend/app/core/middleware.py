import logging
import time
from typing import Callable
import uuid

from fastapi import FastAPI, Request, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.exceptions import AppException
from app.core.logging import correlation_id_ctx
from app.domain.exceptions import (
    DomainException,
    EntityNotFoundException,
    InvalidRecipeStateException,
    RecipeConcurrencyException,
    AccountLockedException,
    AccountDisabledException,
    InvalidCredentialsException,
    TokenReuseDetectedException,
    DuplicateEmailException,
    DuplicateUserNameException,
    ForbiddenDomainException,
)

logger = logging.getLogger("culinary_blog")


async def correlation_id_middleware(
    request: Request, call_next: Callable
) -> Response:
    """FR-OBS-002 / NFR-SEC-006:
    Ensures every request has an X-Correlation-ID header, logs timing, request info, and logs system events.
    """
    correlation_id = request.headers.get("X-Correlation-ID") or str(uuid.uuid4())
    request.state.correlation_id = correlation_id
    token = correlation_id_ctx.set(correlation_id)

    client_ip = (
        request.headers.get("X-Forwarded-For", "").split(",")[0].strip()
        or request.headers.get("X-Real-IP")
        or (request.client.host if request.client else "unknown")
    )

    logger.info(f"Incoming {request.method} {request.url.path} from {client_ip}")
    start_time = time.time()
    try:
        response: Response = await call_next(request)
        process_time = (time.time() - start_time) * 1000  # in ms

        response.headers["X-Correlation-ID"] = correlation_id
        response.headers["X-Response-Time"] = f"{process_time:.2f}ms"

        if process_time > 500:
            logger.warning(
                f"Slow request: {request.method} {request.url.path} took {process_time:.2f}ms (CorrelationID: {correlation_id})"
            )
        else:
            logger.info(
                f"Completed {request.method} {request.url.path} -> {response.status_code} in {process_time:.2f}ms"
            )

        return response
    finally:
        correlation_id_ctx.reset(token)


# In-memory sliding window store for Rate Limiting: { client_ip: [(timestamp, endpoint_type)] }
_rate_limit_records: dict[str, list[tuple[float, str]]] = {}


async def rate_limit_middleware(
    request: Request, call_next: Callable
) -> Response:
    """NFR-SEC-003 Rate Limiting:
    - Auth endpoints (/api/v1/auth/*): 10 req/min
    - Upload endpoints (/images): 5 req/min
    - General API (/api/v1/*): 100 req/min
    Returns HTTP 429 Too Many Requests with Retry-After header and RFC 7807 Problem Details.
    """
    path = request.url.path

    # Only apply rate limiting to /api/ endpoints, skip health and root
    if not path.startswith("/api/"):
        return await call_next(request)

    client_ip = (
        request.headers.get("X-Forwarded-For", "").split(",")[0].strip()
        or request.headers.get("X-Real-IP")
        or (request.client.host if request.client else "127.0.0.1")
    )

    # Determine limit category
    window_seconds = 60
    if "/auth/" in path:
        limit = 10
        category = "auth"
    elif "/images" in path and request.method == "POST":
        limit = 5
        category = "upload"
    else:
        limit = 100
        category = "general"

    now = time.time()
    cutoff = now - window_seconds

    # Clean expired records for this client IP
    records = _rate_limit_records.get(client_ip, [])
    records = [rec for rec in records if rec[0] > cutoff]

    # Count requests for this category
    count = sum(1 for rec in records if rec[1] == category)

    if count >= limit:
        # Earliest timestamp in window
        earliest = min(rec[0] for rec in records if rec[1] == category)
        retry_after = max(1, int(window_seconds - (now - earliest)))
        reset_time = int(earliest + window_seconds)

        logger.warning(f"Rate limit exceeded ({limit} req/min) for IP {client_ip} on {path} [Category: {category}]")
        return JSONResponse(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            headers={
                "Content-Type": "application/problem+json",
                "Retry-After": str(retry_after),
                "X-RateLimit-Limit": str(limit),
                "X-RateLimit-Remaining": "0",
                "X-RateLimit-Reset": str(reset_time),
            },
            content={
                "type": "RATE_LIMIT_EXCEEDED",
                "title": "Too Many Requests",
                "status": status.HTTP_429_TOO_MANY_REQUESTS,
                "detail": f"Quá giới hạn request ({limit} request/phút). Vui lòng thử lại sau {retry_after} giây.",
                "errors": {},
            },
        )

    # Record current request
    records.append((now, category))
    _rate_limit_records[client_ip] = records

    response: Response = await call_next(request)

    # Attach rate limiting headers
    response.headers["X-RateLimit-Limit"] = str(limit)
    response.headers["X-RateLimit-Remaining"] = str(limit - count - 1)
    response.headers["X-RateLimit-Reset"] = str(int(now + window_seconds))

    return response


def register_exception_handlers(app: FastAPI) -> None:
    """Registers custom exception handlers that strictly adhere to RFC 7807 Problem Details.
    Output: { "type": "...", "title": "...", "status": ..., "detail": "...", "errors": {} }
    """

    @app.exception_handler(DomainException)
    async def domain_exception_handler(request: Request, exc: DomainException):
        status_code = status.HTTP_400_BAD_REQUEST
        if isinstance(exc, EntityNotFoundException):
            status_code = status.HTTP_404_NOT_FOUND
        elif isinstance(exc, (InvalidCredentialsException, TokenReuseDetectedException)):
            status_code = status.HTTP_401_UNAUTHORIZED
        elif isinstance(exc, (ForbiddenDomainException, AccountDisabledException)):
            status_code = status.HTTP_403_FORBIDDEN
        elif isinstance(exc, AccountLockedException):
            status_code = status.HTTP_423_LOCKED
        elif isinstance(exc, (DuplicateEmailException, DuplicateUserNameException)):
            status_code = status.HTTP_409_CONFLICT
        elif isinstance(exc, (RecipeConcurrencyException, InvalidRecipeStateException)):
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

        return JSONResponse(
            status_code=status_code,
            headers={"Content-Type": "application/problem+json"},
            content={
                "type": exc.code,
                "title": exc.code.replace("_", " ").title(),
                "status": status_code,
                "detail": exc.message,
                "errors": exc.details,
            },
        )

    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        return JSONResponse(
            status_code=exc.status_code,
            headers={"Content-Type": "application/problem+json"},
            content={
                "type": exc.error_code,
                "title": exc.title,
                "status": exc.status_code,
                "detail": exc.detail,
                "errors": exc.errors,
            },
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        errors = {}
        for err in exc.errors():
            loc = ".".join(str(item) for item in err["loc"] if item != "body")
            field = loc or "non_field_errors"
            if field not in errors:
                errors[field] = []
            errors[field].append(err["msg"])

        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            headers={"Content-Type": "application/problem+json"},
            content={
                "type": "VALIDATION_ERROR",
                "title": "Unprocessable Entity",
                "status": status.HTTP_422_UNPROCESSABLE_ENTITY,
                "detail": "Dữ liệu yêu cầu không hợp lệ.",
                "errors": errors,
            },
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        correlation_id = getattr(request.state, "correlation_id", "unknown")
        logger.error(
            f"Unhandled Exception (CorrelationID: {correlation_id}): {str(exc)}",
            exc_info=True,
        )

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            headers={"Content-Type": "application/problem+json"},
            content={
                "type": "INTERNAL_SERVER_ERROR",
                "title": "Internal Server Error",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "detail": "Đã xảy ra lỗi trong quá trình xử lý yêu cầu. Vui lòng thử lại sau.",
                "errors": {},
            },
        )