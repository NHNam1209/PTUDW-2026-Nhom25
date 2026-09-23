from typing import Any, Dict, Optional
from fastapi import HTTPException, status


class AppException(HTTPException):
    """
    Base application exception that complies with RFC 7807 Problem Details.
    Uses Application Error Codes defined in SRS Appendix B.
    """
    def __init__(
        self,
        status_code: int,
        error_code: str,
        detail: str,
        title: Optional[str] = None,
        errors: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(status_code=status_code, detail=detail)
        self.error_code = error_code
        self.title = title or self._default_title(status_code)
        self.errors = errors or {}

    @staticmethod
    def _default_title(status_code: int) -> str:
        titles = {
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            409: "Conflict",
            422: "Unprocessable Entity",
            423: "Locked",
            429: "Too Many Requests",
            500: "Internal Server Error",
            503: "Service Unavailable",
        }
        return titles.get(status_code, "Error")


class BadRequestException(AppException):
    def __init__(self, error_code: str, detail: str, errors: Optional[Dict[str, Any]] = None):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            error_code=error_code,
            detail=detail,
            title="Bad Request",
            errors=errors
        )


class UnauthorizedException(AppException):
    def __init__(self, error_code: str = "AUTH_TOKEN_INVALID", detail: str = "Unauthorized"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            error_code=error_code,
            detail=detail,
            title="Unauthorized"
        )


class ForbiddenException(AppException):
    def __init__(self, error_code: str = "FORBIDDEN", detail: str = "Forbidden"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            error_code=error_code,
            detail=detail,
            title="Forbidden"
        )


class NotFoundException(AppException):
    def __init__(self, error_code: str, detail: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            error_code=error_code,
            detail=detail,
            title="Not Found"
        )


class ConflictException(AppException):
    def __init__(self, error_code: str, detail: str):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            error_code=error_code,
            detail=detail,
            title="Conflict"
        )


class ConcurrencyConflictException(AppException):
    def __init__(self, detail: str = "Dữ liệu đã bị thay đổi bởi người dùng khác. Vui lòng tải lại trang."):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            error_code="RECIPE_CONCURRENCY_CONFLICT",
            detail=detail,
            title="Concurrency Conflict"
        )
