import logging
import math
from typing import Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy import and_, desc, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user, require_role
from app.core.database import get_db
from app.core.exceptions import BadRequestException, ForbiddenException, NotFoundException
from app.domain.models.recipe import Recipe
from app.domain.models.user import User
from app.schemas.common import PagedMeta, PagedResult
from app.schemas.user import (
    UserListItemDto,
    UserRoleUpdateRequest,
    UserStatusUpdateRequest,
)

logger = logging.getLogger("culinary_blog.users")
audit_logger = logging.getLogger("culinary_blog.audit")

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "",
    response_model=PagedResult[UserListItemDto],
    status_code=status.HTTP_200_OK,
    summary="Xem danh sách người dùng hệ thống (Admin, Tác giả)",
)
async def get_users_list(
    page: int = Query(1, ge=1, description="Số trang (bắt đầu từ 1)"),
    pageSize: int = Query(10, ge=1, le=100, description="Số mục mỗi trang"),
    role: Optional[str] = Query(None, description="Lọc theo vai trò: Admin, Author, User"),
    search: Optional[str] = Query(None, description="Tìm kiếm theo Tên, Username hoặc Email"),
    isActive: Optional[bool] = Query(None, description="Lọc theo trạng thái hoạt động"),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """
    FR-USER-001: Lấy danh sách người dùng cho Admin và Tác giả.
    Hỗ trợ phân trang, tìm kiếm từ khóa, và lọc theo vai trò (Role).
    """
    logger.info(
        f"User {current_user.email} (Role: {current_user.role}) fetching users list with filters: role={role}, search={search}, page={page}"
    )

    query = (
        select(User, func.count(Recipe.id).label("recipe_count"))
        .outerjoin(Recipe, and_(Recipe.author_id == User.id, Recipe.is_deleted == False))
        .group_by(User.id)
    )

    filters = []

    if role:
        filters.append(User.role.ilike(role))

    if isActive is not None:
        filters.append(User.is_active == isActive)

    if search:
        search_term = f"%{search.strip()}%"
        filters.append(
            or_(
                User.full_name.ilike(search_term),
                User.user_name.ilike(search_term),
                User.email.ilike(search_term),
            )
        )

    if filters:
        query = query.where(and_(*filters))

    # Calculate total matching users
    count_subq = (
        select(User.id)
        .where(and_(*filters)) if filters else select(User.id)
    )
    count_stmt = select(func.count()).select_from(count_subq.subquery())
    total_count = (await db.execute(count_stmt)).scalar() or 0

    total_pages = math.ceil(total_count / pageSize) if total_count > 0 else 1
    offset = (page - 1) * pageSize

    query = query.order_by(desc(User.created_at)).offset(offset).limit(pageSize)
    result = await db.execute(query)
    rows = result.all()

    items = []
    for user_row, count in rows:
        item = UserListItemDto(
            id=str(user_row.id),
            fullName=user_row.full_name,
            userName=user_row.user_name,
            email=user_row.email,
            avatarUrl=user_row.avatar_url,
            bio=user_row.bio,
            role=user_row.role or "Author",
            isActive=user_row.is_active,
            emailConfirmed=user_row.email_confirmed,
            recipeCount=count or 0,
            createdAt=user_row.created_at,
        )
        items.append(item)

    return PagedResult(
        items=items,
        meta=PagedMeta(
            page=page,
            pageSize=pageSize,
            totalCount=total_count,
            totalPages=total_pages,
            hasNextPage=page < total_pages,
            hasPreviousPage=page > 1,
        ),
    )


@router.get(
    "/{id}",
    response_model=UserListItemDto,
    status_code=status.HTTP_200_OK,
    summary="Xem chi tiết thông tin người dùng",
)
async def get_user_detail(
    id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    stmt = (
        select(User, func.count(Recipe.id).label("recipe_count"))
        .outerjoin(Recipe, and_(Recipe.author_id == User.id, Recipe.is_deleted == False))
        .where(User.id == id)
        .group_by(User.id)
    )
    result = await db.execute(stmt)
    row = result.first()

    if not row:
        raise NotFoundException(error_code="USER_NOT_FOUND", detail="Không tìm thấy người dùng.")

    user_obj, count = row
    return UserListItemDto(
        id=str(user_obj.id),
        fullName=user_obj.full_name,
        userName=user_obj.user_name,
        email=user_obj.email,
        avatarUrl=user_obj.avatar_url,
        bio=user_obj.bio,
        role=user_obj.role or "Author",
        isActive=user_obj.is_active,
        emailConfirmed=user_obj.email_confirmed,
        recipeCount=count or 0,
        createdAt=user_obj.created_at,
    )


@router.patch(
    "/{id}/role",
    response_model=UserListItemDto,
    status_code=status.HTTP_200_OK,
    summary="Thay đổi vai trò người dùng (Admin only)",
)
async def update_user_role(
    id: str,
    payload: UserRoleUpdateRequest,
    current_user: User = Depends(require_role(["Admin"])),
    db: AsyncSession = Depends(get_db),
):
    stmt = select(User).where(User.id == id)
    user = (await db.execute(stmt)).scalar_one_or_none()
    if not user:
        raise NotFoundException(error_code="USER_NOT_FOUND", detail="Người dùng không tồn tại.")

    old_role = user.role
    user.role = payload.role
    await db.commit()
    await db.refresh(user)

    audit_logger.info(
        f"[AUDIT] Admin {current_user.email} (ID: {current_user.id}) updated role for user {user.email} (ID: {user.id}) from {old_role} to {user.role}"
    )

    # count recipes
    cnt_stmt = select(func.count(Recipe.id)).where(Recipe.author_id == user.id, Recipe.is_deleted == False)
    cnt = (await db.execute(cnt_stmt)).scalar() or 0

    return UserListItemDto(
        id=str(user.id),
        fullName=user.full_name,
        userName=user.user_name,
        email=user.email,
        avatarUrl=user.avatar_url,
        bio=user.bio,
        role=user.role,
        isActive=user.is_active,
        emailConfirmed=user.email_confirmed,
        recipeCount=cnt,
        createdAt=user.created_at,
    )


@router.patch(
    "/{id}/status",
    response_model=UserListItemDto,
    status_code=status.HTTP_200_OK,
    summary="Khóa hoặc mở khóa tài khoản người dùng (Admin only)",
)
async def update_user_status(
    id: str,
    payload: UserStatusUpdateRequest,
    current_user: User = Depends(require_role(["Admin"])),
    db: AsyncSession = Depends(get_db),
):
    stmt = select(User).where(User.id == id)
    user = (await db.execute(stmt)).scalar_one_or_none()
    if not user:
        raise NotFoundException(error_code="USER_NOT_FOUND", detail="Người dùng không tồn tại.")

    if str(user.id) == str(current_user.id):
        raise BadRequestException(
            error_code="CANNOT_LOCK_SELF",
            detail="Bạn không thể tự khóa tài khoản của chính mình."
        )

    old_status = user.is_active
    user.is_active = payload.isActive
    await db.commit()
    await db.refresh(user)

    audit_logger.info(
        f"[AUDIT] Admin {current_user.email} (ID: {current_user.id}) changed status for user {user.email} (ID: {user.id}): is_active {old_status} -> {user.is_active}"
    )

    cnt_stmt = select(func.count(Recipe.id)).where(Recipe.author_id == user.id, Recipe.is_deleted == False)
    cnt = (await db.execute(cnt_stmt)).scalar() or 0

    return UserListItemDto(
        id=str(user.id),
        fullName=user.full_name,
        userName=user.user_name,
        email=user.email,
        avatarUrl=user.avatar_url,
        bio=user.bio,
        role=user.role,
        isActive=user.is_active,
        emailConfirmed=user.email_confirmed,
        recipeCount=cnt,
        createdAt=user.created_at,
    )

