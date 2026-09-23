import secrets
import hashlib
import re
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional, Tuple, Union
import jwt
from passlib.context import CryptContext
from app.core.config import settings
from app.core.exceptions import AppException, UnauthorizedException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify plain password against hashed password."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash password using bcrypt."""
    return pwd_context.hash(password)


def validate_password_strength(password: str) -> Tuple[bool, Optional[str]]:
    """
    Validate password strength according to FR-AUTH-001:
    Tối thiểu 8 ký tự, 1 chữ hoa, 1 chữ thường, 1 chữ số, 1 ký tự đặc biệt.
    """
    if len(password) < 8:
        return False, "Mật khẩu phải có ít nhất 8 ký tự"
    if not re.search(r"[A-Z]", password):
        return False, "Mật khẩu phải chứa ít nhất 1 chữ hoa"
    if not re.search(r"[a-z]", password):
        return False, "Mật khẩu phải chứa ít nhất 1 chữ thường"
    if not re.search(r"\d", password):
        return False, "Mật khẩu phải chứa ít nhất 1 chữ số"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Mật khẩu phải chứa ít nhất 1 ký tự đặc biệt"
    return True, None


def create_access_token(
    user_id: str,
    email: str,
    roles: List[str],
    expires_delta: Optional[timedelta] = None
) -> str:
    """
    Create JWT access token signed with HS256, 15 min TTL (CONS-004, NFR-SEC-002).
    """
    now = datetime.now(timezone.utc)
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "sub": str(user_id),
        "email": email,
        "roles": roles,
        "jti": secrets.token_hex(16),
        "iat": int(now.timestamp()),
        "exp": int(expire.timestamp()),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_access_token(token: str) -> Dict[str, Any]:
    """
    Decode and verify JWT access token.
    Throws UnauthorizedException with appropriate error codes.
    """
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise UnauthorizedException(
            error_code="AUTH_TOKEN_EXPIRED",
            detail="Access token đã hết hạn"
        )
    except jwt.InvalidTokenError:
        raise UnauthorizedException(
            error_code="AUTH_TOKEN_INVALID",
            detail="Access token không hợp lệ"
        )


def generate_refresh_token() -> Tuple[str, str, datetime]:
    """
    Generate cryptographically secure 128-bit random raw token and its SHA-256 hash.
    SRS NFR-SEC-002: Refresh Token is 128-bit random bytes, hashed with SHA-256 before DB storage, TTL 7 days.
    Returns: (raw_token, token_hash, expires_at)
    """
    raw_token = secrets.token_urlsafe(64)
    token_hash = hash_token(raw_token)
    expires_at = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    return raw_token, token_hash, expires_at


def hash_token(token: str) -> str:
    """Hash raw token with SHA-256 for secure storage."""
    return hashlib.sha256(token.encode("utf-8")).hexdigest()
