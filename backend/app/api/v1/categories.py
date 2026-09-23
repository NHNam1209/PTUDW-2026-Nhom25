from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_
from sqlalchemy.orm import selectinload

from app.core.database import get_db
from app.core.exceptions import (
    NotFoundException,
    ConflictException,
    BadRequestException,
)
from app.domain.models.category import Category
from app.domain.models.recipe import Recipe
from app.domain.enums import RecipeStatus
from app.schemas.category import CategoryDto, CategoryCreateDto, CategoryUpdateDto
from app.schemas.recipe import RecipeSummaryDto, RecipeImageDto, RecipeCategorySummaryDto, RecipeAuthorDto
from app.schemas.common import PagedResult, PagedMeta
from app.api.deps import require_role
from app.services.slug import get_unique_slug

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("", response_model=List[CategoryDto], summary="Xem danh sách danh mục (FR-CAT-001)")
async def get_categories(db: AsyncSession = Depends(get_db)):
    stmt = (
        select(Category)
        .where(Category.is_deleted == False)
        .order_by(Category.order_index.asc(), Category.name.asc())
    )
    result = await db.execute(stmt)
    categories = result.scalars().all()

    dtos = []
    for cat in categories:
        count_stmt = select(func.count()).where(
            Recipe.category_id == cat.id,
            Recipe.status == RecipeStatus.Published.value,
            Recipe.is_deleted == False
        )
        count_res = await db.execute(count_stmt)
        count = count_res.scalar_one()

        dtos.append(
            CategoryDto(
                id=cat.id,
                name=cat.name,
                slug=cat.slug,
                description=cat.description,
                imageUrl=cat.image_url,
                orderIndex=cat.order_index,
                recipeCount=count
            )
        )
    return dtos


@router.get("/{slug}", summary="Xem chi tiết danh mục và công thức (FR-CAT-002)")
async def get_category_by_slug(
    slug: str,
    page: int = Query(1, ge=1),
    pageSize: int = Query(12, ge=1, le=50),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Category).where(Category.slug == slug, Category.is_deleted == False)
    res = await db.execute(stmt)
    cat = res.scalar_one_or_none()

    if not cat:
        raise NotFoundException(error_code="CATEGORY_NOT_FOUND", detail=f"Không tìm thấy danh mục '{slug}'.")

    # Get recipes in category
    rcp_stmt = (
        select(Recipe)
        .where(
            Recipe.category_id == cat.id,
            Recipe.status == RecipeStatus.Published.value,
            Recipe.is_deleted == False
        )
        .options(
            selectinload(Recipe.author),
            selectinload(Recipe.images)
        )
        .offset((page - 1) * pageSize)
        .limit(pageSize)
    )
    rcp_res = await db.execute(rcp_stmt)
    recipes = rcp_res.scalars().all()

    count_stmt = select(func.count()).where(
        Recipe.category_id == cat.id,
        Recipe.status == RecipeStatus.Published.value,
        Recipe.is_deleted == False
    )
    total_res = await db.execute(count_stmt)
    total = total_res.scalar_one()
    total_pages = (total + pageSize - 1) // pageSize if total > 0 else 0

    items = []
    for r in recipes:
        p_img = next((img for img in r.images if img.is_primary), None) or (r.images[0] if r.images else None)
        p_img_dto = RecipeImageDto.model_validate(p_img) if p_img else None
        auth_dto = RecipeAuthorDto(id=r.author.id, fullName=r.author.full_name, userName=r.author.user_name, avatarUrl=r.author.avatar_url) if r.author else None

        items.append(
            RecipeSummaryDto(
                id=r.id,
                title=r.title,
                slug=r.slug,
                description=r.description,
                prepTime=r.prep_time,
                cookTime=r.cook_time,
                servings=r.servings,
                difficulty=r.difficulty,
                status=r.status,
                category=RecipeCategorySummaryDto(id=cat.id, name=cat.name, slug=cat.slug),
                author=auth_dto,
                primaryImage=p_img_dto,
                publishedAt=r.published_at,
                createdAt=r.created_at,
            )
        )

    cat_dto = CategoryDto(
        id=cat.id,
        name=cat.name,
        slug=cat.slug,
        description=cat.description,
        imageUrl=cat.image_url,
        orderIndex=cat.order_index,
        recipeCount=total
    )

    return {
        "category": cat_dto,
        "recipes": PagedResult(
            items=items,
            meta=PagedMeta(
                page=page,
                pageSize=pageSize,
                total=total,
                totalPages=total_pages,
                hasNextPage=page < total_pages,
                hasPreviousPage=page > 1
            )
        )
    }


@router.post("", response_model=CategoryDto, status_code=status.HTTP_201_CREATED, summary="Tạo danh mục [Admin] (FR-CAT-003)")
async def create_category(
    req: CategoryCreateDto,
    _=Depends(require_role(["Admin"])),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Category).where(Category.name == req.name, Category.is_deleted == False)
    res = await db.execute(stmt)
    if res.scalar_one_or_none():
        raise ConflictException(error_code="CATEGORY_NAME_EXISTS", detail="Tên danh mục này đã tồn tại.")

    slug = await get_unique_slug(db, Category, req.name)
    category = Category(
        name=req.name,
        slug=slug,
        description=req.description,
        image_url=req.imageUrl,
        order_index=req.orderIndex
    )
    db.add(category)
    await db.commit()
    await db.refresh(category)

    return CategoryDto(
        id=category.id,
        name=category.name,
        slug=category.slug,
        description=category.description,
        imageUrl=category.image_url,
        orderIndex=category.order_index,
        recipeCount=0
    )


@router.put("/{id}", response_model=CategoryDto, summary="Cập nhật danh mục [Admin] (FR-CAT-004)")
async def update_category(
    id: UUID,
    req: CategoryUpdateDto,
    _=Depends(require_role(["Admin"])),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Category).where(Category.id == id, Category.is_deleted == False)
    res = await db.execute(stmt)
    cat = res.scalar_one_or_none()

    if not cat:
        raise NotFoundException(error_code="CATEGORY_NOT_FOUND", detail="Danh mục không tồn tại.")

    if req.name is not None and req.name != cat.name:
        check_name = select(Category).where(Category.name == req.name, Category.id != id, Category.is_deleted == False)
        check_res = await db.execute(check_name)
        if check_res.scalar_one_or_none():
            raise ConflictException(error_code="CATEGORY_NAME_EXISTS", detail="Tên danh mục đã tồn tại.")
        cat.name = req.name

    if req.description is not None:
        cat.description = req.description
    if req.imageUrl is not None:
        cat.image_url = req.imageUrl
    if req.orderIndex is not None:
        cat.order_index = req.orderIndex

    await db.commit()
    await db.refresh(cat)

    return CategoryDto(
        id=cat.id,
        name=cat.name,
        slug=cat.slug,
        description=cat.description,
        imageUrl=cat.image_url,
        orderIndex=cat.order_index,
        recipeCount=0
    )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Xóa danh mục [Admin] (FR-CAT-005)")
async def delete_category(
    id: UUID,
    _=Depends(require_role(["Admin"])),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Category).where(Category.id == id, Category.is_deleted == False)
    res = await db.execute(stmt)
    cat = res.scalar_one_or_none()

    if not cat:
        raise NotFoundException(error_code="CATEGORY_NOT_FOUND", detail="Danh mục không tồn tại.")

    # Business rule: Cannot delete category containing recipes (SRS FR-CAT-005 & CATEGORY_DELETE_HAS_RECIPES)
    count_stmt = select(func.count()).where(Recipe.category_id == id, Recipe.is_deleted == False)
    count_res = await db.execute(count_stmt)
    count = count_res.scalar_one()

    if count > 0:
        raise ConflictException(
            error_code="CATEGORY_DELETE_HAS_RECIPES",
            detail=f"Không thể xóa danh mục đang chứa {count} công thức nấu ăn. Vui lòng chuyển các công thức sang danh mục khác trước."
        )

    await db.delete(cat)
    await db.commit()
    return None
