from typing import Optional, List
from fastapi import Depends, Header
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.core.security import decode_access_token
from app.core.exceptions import UnauthorizedException, ForbiddenException
from app.domain.models.user import User


async def get_current_user(
    authorization: Optional[str] = Header(None),
    db: AsyncSession = Depends(get_db)
) -> User:
    """
    Extracts Bearer token from header and returns authenticated User entity.
    """
    if not authorization or not authorization.startswith("Bearer "):
        raise UnauthorizedException(
            error_code="AUTH_TOKEN_INVALID",
            detail="Thiếu Authorization header Bearer token."
        )

    token = authorization.split(" ")[1]
    payload = decode_access_token(token)
    user_id = payload.get("sub")

    if not user_id:
        raise UnauthorizedException(
            error_code="AUTH_TOKEN_INVALID",
            detail="Token không chứa thông tin người dùng hợp lệ."
        )

    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise UnauthorizedException(
            error_code="AUTH_TOKEN_INVALID",
            detail="Tài khoản không tồn tại hoặc đã bị xóa."
        )

    if not user.is_active:
        raise ForbiddenException(
            error_code="AUTH_ACCOUNT_DISABLED",
            detail="Tài khoản của bạn đã bị khóa bởi Quản trị viên."
        )

    if user.is_locked_out():
        raise ForbiddenException(
            error_code="AUTH_ACCOUNT_LOCKED",
            detail="Tài khoản tạm thời bị khóa do nhiều lần đăng nhập thất bại."
        )

    return user


async def get_current_user_optional(
    authorization: Optional[str] = Header(None),
    db: AsyncSession = Depends(get_db)
) -> Optional[User]:
    """
    Optional authentication: returns User if valid Bearer token provided, None otherwise.
    """
    if not authorization or not authorization.startswith("Bearer "):
        return None

    try:
        return await get_current_user(authorization=authorization, db=db)
    except Exception:
        return None


def require_role(roles: List[str]):
    """
    Role-based access control dependency.
    """
    async def role_checker(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role not in roles:
            raise ForbiddenException(
                error_code="FORBIDDEN",
                detail=f"Quyền truy cập yêu cầu vai trò: {', '.join(roles)}."
            )
        return current_user
    return role_checker
