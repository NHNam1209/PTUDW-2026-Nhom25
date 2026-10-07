"""
Domain Exceptions Layer (Clean Architecture / DDD)
These exceptions represent domain rule violations and are independent of framework-specific concerns.
They are mapped to RFC 7807 Problem Details via the API/Middleware layer.
"""

from typing import Optional, Dict, Any


class DomainException(Exception):
    """Base exception for all domain logic and business rule violations."""
    def __init__(self, message: str, code: str = "DOMAIN_RULE_VIOLATION", details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.message = message
        self.code = code
        self.details = details or {}


class EntityNotFoundException(DomainException):
    """Raised when an aggregate root or entity cannot be found by identifier."""
    def __init__(self, entity_name: str, identifier: Any):
        super().__init__(
            message=f"{entity_name} with identifier '{identifier}' was not found.",
            code=f"{entity_name.upper()}_NOT_FOUND",
            details={"entity": entity_name, "identifier": str(identifier)}
        )


class UserNotFoundException(EntityNotFoundException):
    def __init__(self, identifier: Any):
        super().__init__("User", identifier)


class RecipeNotFoundException(EntityNotFoundException):
    def __init__(self, identifier: Any):
        super().__init__("Recipe", identifier)


class CategoryNotFoundException(EntityNotFoundException):
    def __init__(self, identifier: Any):
        super().__init__("Category", identifier)


class InvalidRecipeStateException(DomainException):
    """Raised when an invalid state transition is attempted on a Recipe aggregate."""
    def __init__(self, message: str, current_status: Optional[int] = None, target_status: Optional[int] = None):
        super().__init__(
            message=message,
            code="RECIPE_INVALID_STATE_TRANSITION",
            details={"current_status": current_status, "target_status": target_status}
        )


class RecipeConcurrencyException(DomainException):
    """Raised when optimistic concurrency conflict occurs (rowVersion mismatch)."""
    def __init__(self, expected_version: int, actual_version: int):
        super().__init__(
            message="Dữ liệu công thức đã bị thay đổi bởi người dùng khác. Vui lòng tải lại trang.",
            code="RECIPE_CONCURRENCY_CONFLICT",
            details={"expected_version": expected_version, "actual_version": actual_version}
        )


class AccountLockedException(DomainException):
    """Raised when an account is locked due to consecutive failed attempts (NFR-SEC-001)."""
    def __init__(self, minutes_remaining: int):
        super().__init__(
            message=f"Tài khoản bị tạm khóa do nhập sai nhiều lần. Vui lòng thử lại sau {minutes_remaining} phút.",
            code="AUTH_ACCOUNT_LOCKED",
            details={"minutes_remaining": minutes_remaining}
        )


class AccountDisabledException(DomainException):
    """Raised when an account has been disabled."""
    def __init__(self):
        super().__init__(
            message="Tài khoản đã bị vô hiệu hóa.",
            code="AUTH_ACCOUNT_DISABLED"
        )


class InvalidCredentialsException(DomainException):
    """Raised for authentication failures without exposing user enumeration."""
    def __init__(self):
        super().__init__(
            message="Email hoặc mật khẩu không chính xác.",
            code="AUTH_INVALID_CREDENTIALS"
        )


class TokenReuseDetectedException(DomainException):
    """Raised when refresh token reuse attack is detected (FR-AUTH-004)."""
    def __init__(self, user_id: str):
        super().__init__(
            message="Phát hiện tái sử dụng Refresh Token bất hợp pháp. Toàn bộ phiên đăng nhập đã bị thu hồi.",
            code="AUTH_TOKEN_REUSE_DETECTED",
            details={"user_id": user_id}
        )


class DuplicateEmailException(DomainException):
    def __init__(self, email: str):
        super().__init__(
            message=f"Email '{email}' đã được đăng ký trong hệ thống.",
            code="AUTH_EMAIL_ALREADY_EXISTS",
            details={"email": email}
        )


class DuplicateUserNameException(DomainException):
    def __init__(self, user_name: str):
        super().__init__(
            message=f"Tên tài khoản '{user_name}' đã tồn tại.",
            code="AUTH_USERNAME_ALREADY_EXISTS",
            details={"user_name": user_name}
        )


class ForbiddenDomainException(DomainException):
    """Raised when a user lacks permission to modify or access a specific domain entity."""
    def __init__(self, action: str, entity_name: str):
        super().__init__(
            message=f"Bạn không có quyền thực hiện thao tác '{action}' trên {entity_name}.",
            code="FORBIDDEN_RESOURCE_ACCESS",
            details={"action": action, "entity": entity_name}
        )
