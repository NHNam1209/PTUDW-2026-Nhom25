import time
import uuid
import logging
from typing import Callable
from fastapi import FastAPI, Request, Response, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.core.exceptions import AppException

logger = logging.getLogger("culinary_blog")


async def correlation_id_middleware(request: Request, call_next: Callable) -> Response:
    """
    FR-OBS-002 / NFR-SEC-006:
    Ensures every request has an X-Correlation-ID header, logs timing and request info.
    """
    correlation_id = request.headers.get("X-Correlation-ID") or str(uuid.uuid4())
    request.state.correlation_id = correlation_id

    start_time = time.time()
    response: Response = await call_next(request)
    process_time = (time.time() - start_time) * 1000  # in ms

    response.headers["X-Correlation-ID"] = correlation_id
    response.headers["X-Response-Time"] = f"{process_time:.2f}ms"

    if process_time > 500:
        logger.warning(
            f"Slow request: {request.method} {request.url.path} took {process_time:.2f}ms (CorrelationID: {correlation_id})"
        )

    return response


def register_exception_handlers(app: FastAPI) -> None:
    """
    Registers custom exception handlers that strictly adhere to RFC 7807 Problem Details.
    Output: { "type": "...", "title": "...", "status": ..., "detail": "...", "errors": {} }
    """
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
            }
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
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
            }
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        correlation_id = getattr(request.state, "correlation_id", "unknown")
        logger.error(f"Unhandled Exception (CorrelationID: {correlation_id}): {str(exc)}", exc_info=True)

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            headers={"Content-Type": "application/problem+json"},
            content={
                "type": "INTERNAL_SERVER_ERROR",
                "title": "Internal Server Error",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "detail": "Đã xảy ra lỗi trong quá trình xử lý yêu cầu. Vui lòng thử lại sau.",
                "errors": {},
            }
        )
