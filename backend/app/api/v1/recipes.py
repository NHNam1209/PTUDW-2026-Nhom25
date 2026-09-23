import math
from datetime import datetime, timezone
from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, Query, UploadFile, File, Form, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_, or_, desc, asc
from sqlalchemy.orm import selectinload

from app.core.database import get_db
from app.core.exceptions import (
    NotFoundException,
    ForbiddenException,
    ConflictException,
    BadRequestException,
    ConcurrencyConflictException,
)
from app.domain.enums import RecipeStatus, RecipeDifficulty
from app.domain.models.recipe import Recipe
from app.domain.models.category import Category
from app.domain.models.user import User
from app.domain.models.recipe_step import RecipeStep
from app.domain.models.recipe_ingredient import RecipeIngredient
from app.domain.models.recipe_image import RecipeImage
from app.schemas.common import PagedResult, PagedMeta
from app.schemas.recipe import (
    RecipeSummaryDto,
    RecipeDetailDto,
    RecipeCreateDto,
    RecipeUpdateDto,
    RecipeStepDto,
    RecipeStepCreateDto,
    RecipeIngredientDto,
    RecipeIngredientCreateDto,
    RecipeImageDto,
    RecipeNutritionDto,
    RecipeAuthorDto,
    RecipeCategorySummaryDto,
)
from app.api.deps import get_current_user, get_current_user_optional, require_role
from app.services.slug import get_unique_slug
from app.services.storage import storage_service

router = APIRouter(prefix="/recipes", tags=["Recipes"])


def _check_recipe_ownership(recipe: Recipe, user: User) -> None:
    """Verifies that current user is the owner or Admin."""
    if user.role != "Admin" and str(recipe.author_id) != str(user.id):
        raise ForbiddenException(
            error_code="RECIPE_FORBIDDEN",
            detail="Bạn không có quyền chỉnh sửa hoặc xóa công thức này."
        )


def _to_detail_dto(recipe: Recipe) -> RecipeDetailDto:
    primary_img = next((img for img in recipe.images if img.is_primary), None)
    if not primary_img and recipe.images:
        primary_img = recipe.images[0]

    primary_img_dto = RecipeImageDto.model_validate(primary_img) if primary_img else None

    category_dto = None
    if recipe.category:
        category_dto = RecipeCategorySummaryDto(
            id=recipe.category.id,
            name=recipe.category.name,
            slug=recipe.category.slug,
        )

    author_dto = None
    if recipe.author:
        author_dto = RecipeAuthorDto(
            id=recipe.author.id,
            fullName=recipe.author.full_name,
            userName=recipe.author.user_name,
            avatarUrl=recipe.author.avatar_url,
        )

    nutrition_dto = RecipeNutritionDto(
        calories=recipe.nutrition_calories,
        protein=recipe.nutrition_protein,
        carbohydrates=recipe.nutrition_carbohydrates,
        fat=recipe.nutrition_fat,
        fiber=recipe.nutrition_fiber,
        sodium=recipe.nutrition_sodium,
    )

    steps_dto = [RecipeStepDto.model_validate(s) for s in recipe.steps]
    ingredients_dto = [RecipeIngredientDto.model_validate(i) for i in recipe.ingredients]
    images_dto = [RecipeImageDto.model_validate(img) for img in recipe.images]

    return RecipeDetailDto(
        id=recipe.id,
        title=recipe.title,
        slug=recipe.slug,
        description=recipe.description,
        instructions=recipe.instructions,
        prepTime=recipe.prep_time,
        cookTime=recipe.cook_time,
        servings=recipe.servings,
        difficulty=recipe.difficulty,
        status=recipe.status,
        category=category_dto,
        author=author_dto,
        primaryImage=primary_img_dto,
        publishedAt=recipe.published_at,
        createdAt=recipe.created_at,
        nutrition=nutrition_dto,
        steps=steps_dto,
        ingredients=ingredients_dto,
        images=images_dto,
        rowVersion=recipe.row_version,
    )


# -------------------------------------------------------------
# FR-RCP-001: Xem Danh sách Công thức (Paginated + Filtered + Sorted)
# -------------------------------------------------------------
@router.get(
    "",
    response_model=PagedResult[RecipeSummaryDto],
    status_code=status.HTTP_200_OK,
    summary="Xem danh sách công thức nấu ăn (FR-RCP-001)"
)
async def get_recipes(
    page: int = Query(1, ge=1),
    pageSize: int = Query(12, ge=1, le=50),
    categoryId: Optional[UUID] = Query(None),
    difficulty: Optional[int] = Query(None, ge=1, le=4),
    maxCookTime: Optional[int] = Query(None, ge=0),
    sort: str = Query("-createdAt"),
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(Recipe)
        .where(Recipe.is_deleted == False)
        .options(
            selectinload(Recipe.category),
            selectinload(Recipe.author),
            selectinload(Recipe.images),
        )
    )

    # 1. Authorization filter
    if not current_user:
        stmt = stmt.where(Recipe.status == RecipeStatus.Published.value)
    elif current_user.role == "Admin":
        pass  # Admin sees all statuses
    else:
        # Author sees published + their own drafts/archived
        stmt = stmt.where(
            or_(
                Recipe.status == RecipeStatus.Published.value,
                and_(
                    Recipe.author_id == current_user.id,
                    Recipe.status.in_([RecipeStatus.Draft.value, RecipeStatus.Archived.value])
                )
            )
        )

    # 2. Filters
    if categoryId:
        stmt = stmt.where(Recipe.category_id == categoryId)
    if difficulty:
        stmt = stmt.where(Recipe.difficulty == difficulty)
    if maxCookTime is not None:
        stmt = stmt.where(Recipe.cook_time <= maxCookTime)

    # 3. Total count query
    count_stmt = select(func.count()).select_from(stmt.subquery())
    total_res = await db.execute(count_stmt)
    total_count = total_res.scalar_one()

    # 4. Sorting
    sort_mapping = {
        "-createdAt": desc(Recipe.created_at),
        "createdAt": asc(Recipe.created_at),
        "title": asc(Recipe.title),
        "-title": desc(Recipe.title),
        "cookTime": asc(Recipe.cook_time),
        "-cookTime": desc(Recipe.cook_time),
    }
    order_clause = sort_mapping.get(sort, desc(Recipe.created_at))
    stmt = stmt.order_by(order_clause)

    # 5. Pagination
    stmt = stmt.offset((page - 1) * pageSize).limit(pageSize)
    result = await db.execute(stmt)
    recipes = result.scalars().all()

    items: List[RecipeSummaryDto] = []
    for r in recipes:
        p_img = next((img for img in r.images if img.is_primary), None) or (r.images[0] if r.images else None)
        p_img_dto = RecipeImageDto.model_validate(p_img) if p_img else None

        cat_dto = RecipeCategorySummaryDto(id=r.category.id, name=r.category.name, slug=r.category.slug) if r.category else None
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
                category=cat_dto,
                author=auth_dto,
                primaryImage=p_img_dto,
                publishedAt=r.published_at,
                createdAt=r.created_at,
            )
        )

    total_pages = math.ceil(total_count / pageSize) if total_count > 0 else 0

    return PagedResult(
        items=items,
        meta=PagedMeta(
            page=page,
            pageSize=pageSize,
            total=total_count,
            totalPages=total_pages,
            hasNextPage=page < total_pages,
            hasPreviousPage=page > 1,
        )
    )


# -------------------------------------------------------------
# FR-RCP-002: Xem Chi tiết Công thức
# -------------------------------------------------------------
@router.get(
    "/{slug_or_id}",
    response_model=RecipeDetailDto,
    status_code=status.HTTP_200_OK,
    summary="Xem chi tiết công thức nấu ăn (FR-RCP-002)"
)
async def get_recipe_detail(
    slug_or_id: str,
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(Recipe)
        .where(Recipe.is_deleted == False)
        .options(
            selectinload(Recipe.category),
            selectinload(Recipe.author),
            selectinload(Recipe.steps),
            selectinload(Recipe.ingredients),
            selectinload(Recipe.images),
        )
    )

    # Allow query by slug or UUID
    try:
        val_uuid = UUID(slug_or_id)
        stmt = stmt.where(Recipe.id == val_uuid)
    except ValueError:
        stmt = stmt.where(Recipe.slug == slug_or_id)

    res = await db.execute(stmt)
    recipe = res.scalar_one_or_none()

    if not recipe:
        raise NotFoundException(
            error_code="RECIPE_NOT_FOUND",
            detail=f"Không tìm thấy công thức với định danh '{slug_or_id}'."
        )

    # Authorization for Draft/Archived
    if recipe.status != RecipeStatus.Published.value:
        if not current_user:
            raise ForbiddenException(
                error_code="RECIPE_FORBIDDEN",
                detail="Công thức này chưa được xuất bản. Vui lòng đăng nhập để xem."
            )
        _check_recipe_ownership(recipe, current_user)

    return _to_detail_dto(recipe)


# -------------------------------------------------------------
# FR-RCP-003: Tạo Công thức Nấu ăn Mới [Author/Admin]
# -------------------------------------------------------------
@router.post(
    "",
    response_model=RecipeDetailDto,
    status_code=status.HTTP_201_CREATED,
    summary="Tạo công thức mới (FR-RCP-003)"
)
async def create_recipe(
    req: RecipeCreateDto,
    current_user: User = Depends(require_role(["Author", "Admin"])),
    db: AsyncSession = Depends(get_db)
):
    # Verify category exists
    cat_stmt = select(Category).where(Category.id == req.categoryId, Category.is_deleted == False)
    cat_res = await db.execute(cat_stmt)
    category = cat_res.scalar_one_or_none()
    if not category:
        raise BadRequestException(
            error_code="VALIDATION_ERROR",
            detail="Danh mục (categoryId) không tồn tại."
        )

    # Generate unique slug
    slug = await get_unique_slug(db, Recipe, req.title)

    recipe = Recipe(
        title=req.title,
        slug=slug,
        description=req.description,
        instructions=req.instructions or "",
        prep_time=req.prepTimeMinutes,
        cook_time=req.cookTimeMinutes,
        servings=req.servings,
        difficulty=req.difficulty,
        status=RecipeStatus.Draft.value,
        category_id=req.categoryId,
        author_id=current_user.id,
    )

    if req.nutrition:
        recipe.nutrition_calories = req.nutrition.calories
        recipe.nutrition_protein = req.nutrition.protein
        recipe.nutrition_carbohydrates = req.nutrition.carbohydrates
        recipe.nutrition_fat = req.nutrition.fat
        recipe.nutrition_fiber = req.nutrition.fiber
        recipe.nutrition_sodium = req.nutrition.sodium

    db.add(recipe)
    await db.flush()

    # Steps
    if req.steps:
        for idx, s in enumerate(req.steps, 1):
            step = RecipeStep(
                recipe_id=recipe.id,
                step_number=idx,
                title=s.title,
                description=s.description,
                timer_minutes=s.timerMinutes,
                image_url=s.imageUrl,
            )
            db.add(step)

    # Ingredients
    if req.ingredients:
        for idx, ing in enumerate(req.ingredients):
            ingredient = RecipeIngredient(
                recipe_id=recipe.id,
                name=ing.name,
                quantity=ing.quantity,
                unit=ing.unit,
                notes=ing.notes,
                order_index=idx,
            )
            db.add(ingredient)

    await db.commit()

    # Reload with relations
    stmt_reload = (
        select(Recipe)
        .where(Recipe.id == recipe.id)
        .options(
            selectinload(Recipe.category),
            selectinload(Recipe.author),
            selectinload(Recipe.steps),
            selectinload(Recipe.ingredients),
            selectinload(Recipe.images),
        )
    )
    res_reload = await db.execute(stmt_reload)
    return _to_detail_dto(res_reload.scalar_one())


# -------------------------------------------------------------
# FR-RCP-004: Cập nhật Công thức [Author-Owner/Admin]
# -------------------------------------------------------------
@router.put(
    "/{id}",
    response_model=RecipeDetailDto,
    status_code=status.HTTP_200_OK,
    summary="Cập nhật thông tin công thức (FR-RCP-004)"
)
async def update_recipe(
    id: UUID,
    req: RecipeUpdateDto,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(Recipe)
        .where(Recipe.id == id, Recipe.is_deleted == False)
        .options(
            selectinload(Recipe.category),
            selectinload(Recipe.author),
            selectinload(Recipe.steps),
            selectinload(Recipe.ingredients),
            selectinload(Recipe.images),
        )
    )
    res = await db.execute(stmt)
    recipe = res.scalar_one_or_none()

    if not recipe:
        raise NotFoundException(
            error_code="RECIPE_NOT_FOUND",
            detail="Công thức không tồn tại."
        )

    _check_recipe_ownership(recipe, current_user)

    # Optimistic Concurrency Check (SRS CONS-004, NFR-REL-003, RECIPE_CONCURRENCY_CONFLICT)
    if req.rowVersion is not None and req.rowVersion != recipe.row_version:
        raise ConcurrencyConflictException()

    if req.categoryId:
        cat_stmt = select(Category).where(Category.id == req.categoryId, Category.is_deleted == False)
        cat_res = await db.execute(cat_stmt)
        if not cat_res.scalar_one_or_none():
            raise BadRequestException(error_code="VALIDATION_ERROR", detail="CategoryId không tồn tại.")
        recipe.category_id = req.categoryId

    if req.title and req.title != recipe.title:
        recipe.title = req.title
        # Regenerate slug if still draft
        if recipe.status == RecipeStatus.Draft.value:
            recipe.slug = await get_unique_slug(db, Recipe, req.title, current_id=recipe.id)

    if req.description is not None:
        recipe.description = req.description
    if req.instructions is not None:
        recipe.instructions = req.instructions
    if req.prepTimeMinutes is not None:
        recipe.prep_time = req.prepTimeMinutes
    if req.cookTimeMinutes is not None:
        recipe.cook_time = req.cookTimeMinutes
    if req.servings is not None:
        recipe.servings = req.servings
    if req.difficulty is not None:
        recipe.difficulty = req.difficulty

    if req.nutrition:
        recipe.nutrition_calories = req.nutrition.calories
        recipe.nutrition_protein = req.nutrition.protein
        recipe.nutrition_carbohydrates = req.nutrition.carbohydrates
        recipe.nutrition_fat = req.nutrition.fat
        recipe.nutrition_fiber = req.nutrition.fiber
        recipe.nutrition_sodium = req.nutrition.sodium

    recipe.row_version += 1
    recipe.updated_at = datetime.now(timezone.utc)

    await db.commit()
    await db.refresh(recipe)
    return _to_detail_dto(recipe)


# -------------------------------------------------------------
# FR-RCP-005: Xuất bản / Hủy Xuất bản Công thức
# -------------------------------------------------------------
@router.patch(
    "/{id}/publish",
    response_model=RecipeDetailDto,
    status_code=status.HTTP_200_OK,
    summary="Xuất bản công thức (FR-RCP-005)"
)
async def publish_recipe(
    id: UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(Recipe)
        .where(Recipe.id == id, Recipe.is_deleted == False)
        .options(
            selectinload(Recipe.category),
            selectinload(Recipe.author),
            selectinload(Recipe.steps),
            selectinload(Recipe.ingredients),
            selectinload(Recipe.images),
        )
    )
    res = await db.execute(stmt)
    recipe = res.scalar_one_or_none()

    if not recipe:
        raise NotFoundException(error_code="RECIPE_NOT_FOUND", detail="Công thức không tồn tại.")

    _check_recipe_ownership(recipe, current_user)

    # Business rule: Must have at least 1 step and 1 ingredient (SRS FR-RCP-005 & Appendix B RECIPE_PUBLISH_INCOMPLETE)
    if len(recipe.steps) == 0 or len(recipe.ingredients) == 0:
        raise BadRequestException(
            error_code="RECIPE_PUBLISH_INCOMPLETE",
            detail="Recipe phải có ít nhất 1 bước thực hiện và 1 nguyên liệu mới có thể xuất bản."
        )

    recipe.status = RecipeStatus.Published.value
    recipe.published_at = datetime.now(timezone.utc)
    recipe.row_version += 1

    await db.commit()
    await db.refresh(recipe)
    return _to_detail_dto(recipe)


@router.patch(
    "/{id}/unpublish",
    response_model=RecipeDetailDto,
    status_code=status.HTTP_200_OK,
    summary="Hủy xuất bản công thức (FR-RCP-005)"
)
async def unpublish_recipe(
    id: UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(Recipe)
        .where(Recipe.id == id, Recipe.is_deleted == False)
        .options(
            selectinload(Recipe.category),
            selectinload(Recipe.author),
            selectinload(Recipe.steps),
            selectinload(Recipe.ingredients),
            selectinload(Recipe.images),
        )
    )
    res = await db.execute(stmt)
    recipe = res.scalar_one_or_none()

    if not recipe:
        raise NotFoundException(error_code="RECIPE_NOT_FOUND", detail="Công thức không tồn tại.")

    _check_recipe_ownership(recipe, current_user)

    recipe.status = RecipeStatus.Draft.value
    recipe.row_version += 1

    await db.commit()
    await db.refresh(recipe)
    return _to_detail_dto(recipe)


# -------------------------------------------------------------
# FR-RCP-006: Lưu trữ Công thức (Archive)
# -------------------------------------------------------------
@router.patch(
    "/{id}/archive",
    response_model=RecipeDetailDto,
    status_code=status.HTTP_200_OK,
    summary="Lưu trữ công thức (FR-RCP-006)"
)
async def archive_recipe(
    id: UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(Recipe)
        .where(Recipe.id == id, Recipe.is_deleted == False)
        .options(
            selectinload(Recipe.category),
            selectinload(Recipe.author),
            selectinload(Recipe.steps),
            selectinload(Recipe.ingredients),
            selectinload(Recipe.images),
        )
    )
    res = await db.execute(stmt)
    recipe = res.scalar_one_or_none()

    if not recipe:
        raise NotFoundException(error_code="RECIPE_NOT_FOUND", detail="Công thức không tồn tại.")

    _check_recipe_ownership(recipe, current_user)

    recipe.status = RecipeStatus.Archived.value
    recipe.row_version += 1

    await db.commit()
    await db.refresh(recipe)
    return _to_detail_dto(recipe)


# -------------------------------------------------------------
# FR-RCP-007: Xóa Công thức [Author-Owner/Admin]
# -------------------------------------------------------------
@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Xóa công thức nấu ăn (FR-RCP-007)"
)
async def delete_recipe(
    id: UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(Recipe)
        .where(Recipe.id == id, Recipe.is_deleted == False)
        .options(selectinload(Recipe.images))
    )
    res = await db.execute(stmt)
    recipe = res.scalar_one_or_none()

    if not recipe:
        raise NotFoundException(error_code="RECIPE_NOT_FOUND", detail="Công thức không tồn tại.")

    _check_recipe_ownership(recipe, current_user)

    # Clean up images in MinIO
    for img in recipe.images:
        await storage_service.delete_file(img.original_url)

    await db.delete(recipe)
    await db.commit()
    return None


# -------------------------------------------------------------
# FR-RCP-008: Quản lý Ảnh Công thức (Upload / Set Primary / Delete)
# -------------------------------------------------------------
@router.post(
    "/{id}/images",
    response_model=RecipeImageDto,
    status_code=status.HTTP_201_CREATED,
    summary="Upload ảnh công thức (FR-RCP-008)"
)
async def upload_recipe_image(
    id: UUID,
    file: UploadFile = File(...),
    altText: Optional[str] = Form(None),
    isPrimary: bool = Form(False),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(Recipe)
        .where(Recipe.id == id, Recipe.is_deleted == False)
        .options(selectinload(Recipe.images))
    )
    res = await db.execute(stmt)
    recipe = res.scalar_one_or_none()

    if not recipe:
        raise NotFoundException(error_code="RECIPE_NOT_FOUND", detail="Công thức không tồn tại.")

    _check_recipe_ownership(recipe, current_user)

    # Upload to MinIO
    uploaded_url = await storage_service.upload_file(file, folder=f"recipes/{id}")

    # Set as primary if requested or if it's the only image
    should_be_primary = isPrimary or len(recipe.images) == 0
    if should_be_primary:
        for existing_img in recipe.images:
            existing_img.is_primary = False

    new_img = RecipeImage(
        recipe_id=recipe.id,
        original_url=uploaded_url,
        alt_text=altText,
        is_primary=should_be_primary,
        order_index=len(recipe.images),
    )
    db.add(new_img)
    await db.commit()
    await db.refresh(new_img)

    return RecipeImageDto.model_validate(new_img)


@router.patch(
    "/{id}/images/{image_id}/primary",
    response_model=RecipeImageDto,
    status_code=status.HTTP_200_OK,
    summary="Đặt ảnh chính cho công thức (FR-RCP-008)"
)
async def set_primary_image(
    id: UUID,
    image_id: UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(Recipe)
        .where(Recipe.id == id, Recipe.is_deleted == False)
        .options(selectinload(Recipe.images))
    )
    res = await db.execute(stmt)
    recipe = res.scalar_one_or_none()

    if not recipe:
        raise NotFoundException(error_code="RECIPE_NOT_FOUND", detail="Công thức không tồn tại.")

    _check_recipe_ownership(recipe, current_user)

    target_img = None
    for img in recipe.images:
        if img.id == image_id:
            img.is_primary = True
            target_img = img
        else:
            img.is_primary = False

    if not target_img:
        raise NotFoundException(error_code="IMAGE_NOT_FOUND", detail="Không tìm thấy ảnh này trong công thức.")

    await db.commit()
    await db.refresh(target_img)
    return RecipeImageDto.model_validate(target_img)


@router.delete(
    "/{id}/images/{image_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Xóa ảnh công thức (FR-RCP-008)"
)
async def delete_recipe_image(
    id: UUID,
    image_id: UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(Recipe)
        .where(Recipe.id == id, Recipe.is_deleted == False)
        .options(selectinload(Recipe.images))
    )
    res = await db.execute(stmt)
    recipe = res.scalar_one_or_none()

    if not recipe:
        raise NotFoundException(error_code="RECIPE_NOT_FOUND", detail="Công thức không tồn tại.")

    _check_recipe_ownership(recipe, current_user)

    target_img = next((img for img in recipe.images if img.id == image_id), None)
    if not target_img:
        raise NotFoundException(error_code="IMAGE_NOT_FOUND", detail="Không tìm thấy ảnh.")

    was_primary = target_img.is_primary
    file_url = target_img.original_url

    await db.delete(target_img)
    await storage_service.delete_file(file_url)

    # If deleted image was primary, assign first remaining as primary
    remaining = [img for img in recipe.images if img.id != image_id]
    if was_primary and remaining:
        remaining[0].is_primary = True

    await db.commit()
    return None


# -------------------------------------------------------------
# FR-RCP-009: Quản lý Nguyên liệu (CRUD RecipeIngredient)
# -------------------------------------------------------------
@router.post(
    "/{id}/ingredients",
    response_model=RecipeIngredientDto,
    status_code=status.HTTP_201_CREATED,
    summary="Thêm nguyên liệu vào công thức (FR-RCP-009)"
)
async def add_recipe_ingredient(
    id: UUID,
    req: RecipeIngredientCreateDto,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(Recipe)
        .where(Recipe.id == id, Recipe.is_deleted == False)
        .options(selectinload(Recipe.ingredients))
    )
    res = await db.execute(stmt)
    recipe = res.scalar_one_or_none()

    if not recipe:
        raise NotFoundException(error_code="RECIPE_NOT_FOUND", detail="Công thức không tồn tại.")

    _check_recipe_ownership(recipe, current_user)

    new_ing = RecipeIngredient(
        recipe_id=recipe.id,
        name=req.name,
        quantity=req.quantity,
        unit=req.unit,
        notes=req.notes,
        order_index=req.orderIndex or len(recipe.ingredients),
    )
    db.add(new_ing)
    await db.commit()
    await db.refresh(new_ing)
    return RecipeIngredientDto.model_validate(new_ing)


@router.put(
    "/{id}/ingredients/{ingredient_id}",
    response_model=RecipeIngredientDto,
    status_code=status.HTTP_200_OK,
    summary="Cập nhật nguyên liệu (FR-RCP-009)"
)
async def update_recipe_ingredient(
    id: UUID,
    ingredient_id: UUID,
    req: RecipeIngredientCreateDto,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Recipe).where(Recipe.id == id, Recipe.is_deleted == False)
    res = await db.execute(stmt)
    recipe = res.scalar_one_or_none()

    if not recipe:
        raise NotFoundException(error_code="RECIPE_NOT_FOUND", detail="Công thức không tồn tại.")

    _check_recipe_ownership(recipe, current_user)

    stmt_ing = select(RecipeIngredient).where(RecipeIngredient.id == ingredient_id, RecipeIngredient.recipe_id == id)
    res_ing = await db.execute(stmt_ing)
    ing = res_ing.scalar_one_or_none()

    if not ing:
        raise NotFoundException(error_code="INGREDIENT_NOT_FOUND", detail="Không tìm thấy nguyên liệu.")

    ing.name = req.name
    ing.quantity = req.quantity
    ing.unit = req.unit
    ing.notes = req.notes
    ing.order_index = req.orderIndex

    await db.commit()
    await db.refresh(ing)
    return RecipeIngredientDto.model_validate(ing)


@router.delete(
    "/{id}/ingredients/{ingredient_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Xóa nguyên liệu (FR-RCP-009)"
)
async def delete_recipe_ingredient(
    id: UUID,
    ingredient_id: UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Recipe).where(Recipe.id == id, Recipe.is_deleted == False)
    res = await db.execute(stmt)
    recipe = res.scalar_one_or_none()

    if not recipe:
        raise NotFoundException(error_code="RECIPE_NOT_FOUND", detail="Công thức không tồn tại.")

    _check_recipe_ownership(recipe, current_user)

    stmt_ing = select(RecipeIngredient).where(RecipeIngredient.id == ingredient_id, RecipeIngredient.recipe_id == id)
    res_ing = await db.execute(stmt_ing)
    ing = res_ing.scalar_one_or_none()

    if not ing:
        raise NotFoundException(error_code="INGREDIENT_NOT_FOUND", detail="Không tìm thấy nguyên liệu.")

    await db.delete(ing)
    await db.commit()
    return None


# -------------------------------------------------------------
# FR-RCP-010: Quản lý Các bước Thực hiện (CRUD RecipeStep)
# -------------------------------------------------------------
@router.post(
    "/{id}/steps",
    response_model=RecipeStepDto,
    status_code=status.HTTP_201_CREATED,
    summary="Thêm bước thực hiện (FR-RCP-010)"
)
async def add_recipe_step(
    id: UUID,
    req: RecipeStepCreateDto,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(Recipe)
        .where(Recipe.id == id, Recipe.is_deleted == False)
        .options(selectinload(Recipe.steps))
    )
    res = await db.execute(stmt)
    recipe = res.scalar_one_or_none()

    if not recipe:
        raise NotFoundException(error_code="RECIPE_NOT_FOUND", detail="Công thức không tồn tại.")

    _check_recipe_ownership(recipe, current_user)

    # Auto step number: max(step_number) + 1
    next_step_num = (max((s.step_number for s in recipe.steps), default=0)) + 1

    new_step = RecipeStep(
        recipe_id=recipe.id,
        step_number=next_step_num,
        title=req.title,
        description=req.description,
        timer_minutes=req.timerMinutes,
        image_url=req.imageUrl,
    )
    db.add(new_step)
    await db.commit()
    await db.refresh(new_step)
    return RecipeStepDto.model_validate(new_step)


@router.put(
    "/{id}/steps/{step_id}",
    response_model=RecipeStepDto,
    status_code=status.HTTP_200_OK,
    summary="Cập nhật bước thực hiện (FR-RCP-010)"
)
async def update_recipe_step(
    id: UUID,
    step_id: UUID,
    req: RecipeStepCreateDto,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Recipe).where(Recipe.id == id, Recipe.is_deleted == False)
    res = await db.execute(stmt)
    recipe = res.scalar_one_or_none()

    if not recipe:
        raise NotFoundException(error_code="RECIPE_NOT_FOUND", detail="Công thức không tồn tại.")

    _check_recipe_ownership(recipe, current_user)

    stmt_step = select(RecipeStep).where(RecipeStep.id == step_id, RecipeStep.recipe_id == id)
    res_step = await db.execute(stmt_step)
    step = res_step.scalar_one_or_none()

    if not step:
        raise NotFoundException(error_code="STEP_NOT_FOUND", detail="Không tìm thấy bước này.")

    step.title = req.title
    step.description = req.description
    step.timer_minutes = req.timerMinutes
    if req.imageUrl is not None:
        step.image_url = req.imageUrl

    await db.commit()
    await db.refresh(step)
    return RecipeStepDto.model_validate(step)


@router.delete(
    "/{id}/steps/{step_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Xóa bước thực hiện và renumber (FR-RCP-010)"
)
async def delete_recipe_step(
    id: UUID,
    step_id: UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = (
        select(Recipe)
        .where(Recipe.id == id, Recipe.is_deleted == False)
        .options(selectinload(Recipe.steps))
    )
    res = await db.execute(stmt)
    recipe = res.scalar_one_or_none()

    if not recipe:
        raise NotFoundException(error_code="RECIPE_NOT_FOUND", detail="Công thức không tồn tại.")

    _check_recipe_ownership(recipe, current_user)

    target_step = next((s for s in recipe.steps if s.id == step_id), None)
    if not target_step:
        raise NotFoundException(error_code="STEP_NOT_FOUND", detail="Không tìm thấy bước cần xóa.")

    await db.delete(target_step)

    # Renumber remaining steps consecutively (1, 2, 3...) as required in FR-RCP-010
    remaining_steps = sorted(
        [s for s in recipe.steps if s.id != step_id],
        key=lambda x: x.step_number
    )
    for idx, s in enumerate(remaining_steps, 1):
        s.step_number = idx

    await db.commit()
    return None
