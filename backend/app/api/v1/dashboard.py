from datetime import datetime, timezone, timedelta
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_, desc
from sqlalchemy.orm import selectinload
from pydantic import BaseModel, Field

from app.core.database import get_db
from app.domain.enums import RecipeStatus, RecipeDifficulty
from app.domain.models.recipe import Recipe
from app.domain.models.category import Category
from app.domain.models.user import User
from app.api.deps import get_current_user
from app.schemas.recipe import RecipeImageDto

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


class DashboardStatsDto(BaseModel):
    totalRecipes: int = Field(..., description="Total number of recipes")
    publishedCount: int = Field(..., description="Number of published recipes")
    draftCount: int = Field(..., description="Number of draft recipes")
    archivedCount: int = Field(..., description="Number of archived recipes")
    recentRecipes: List[dict] = Field(..., description="5 most recent recipes")
    categoryDistribution: List[dict] = Field(..., description="Recipe count by category")
    difficultyDistribution: List[dict] = Field(..., description="Recipe count by difficulty")


class RecentRecipeDto(BaseModel):
    id: str
    title: str
    slug: str
    status: int
    category: str
    createdAt: datetime
    primaryImageUrl: str | None = None


class CategoryStatsDto(BaseModel):
    categoryId: str
    categoryName: str
    categorySlug: str
    recipeCount: int


class DifficultyStatsDto(BaseModel):
    difficulty: int
    difficultyLabel: str
    count: int


@router.get(
    "/stats",
    response_model=DashboardStatsDto,
    status_code=status.HTTP_200_OK,
    summary="Get dashboard statistics (FR-DASH-001)"
)
async def get_dashboard_stats(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Returns dashboard overview statistics for the current user:
    - Total recipes and counts by status
    - 5 most recent recipes
    - Category distribution
    - Difficulty distribution
    """
    # Base query: user's recipes (Admin sees all, Author sees own)
    base_filter = Recipe.is_deleted == False
    if current_user.role != "Admin":
        base_filter = and_(Recipe.is_deleted == False, Recipe.author_id == current_user.id)

    # 1. Status counts
    status_counts_stmt = (
        select(Recipe.status, func.count(Recipe.id))
        .where(base_filter)
        .group_by(Recipe.status)
    )
    status_result = await db.execute(status_counts_stmt)
    status_counts = {row[0]: row[1] for row in status_result.all()}

    total_recipes = sum(status_counts.values())
    published_count = status_counts.get(RecipeStatus.Published.value, 0)
    draft_count = status_counts.get(RecipeStatus.Draft.value, 0)
    archived_count = status_counts.get(RecipeStatus.Archived.value, 0)

    # 2. Recent recipes (last 5)
    recent_stmt = (
        select(Recipe)
        .where(base_filter)
        .options(
            selectinload(Recipe.category),
            selectinload(Recipe.images),
        )
        .order_by(desc(Recipe.created_at))
        .limit(5)
    )
    recent_result = await db.execute(recent_stmt)
    recent_recipes = recent_result.scalars().all()

    recent_recipes_dto = []
    for r in recent_recipes:
        primary_img = next((img for img in r.images if img.is_primary), None)
        if not primary_img and r.images:
            primary_img = r.images[0]
        
        recent_recipes_dto.append({
            "id": str(r.id),
            "title": r.title,
            "slug": r.slug,
            "status": r.status,
            "category": r.category.name if r.category else "Chưa phân loại",
            "createdAt": r.created_at.isoformat() if r.created_at else None,
            "primaryImageUrl": primary_img.original_url if primary_img else None,
        })

    # 3. Category distribution
    category_stmt = (
        select(
            Category.id,
            Category.name,
            Category.slug,
            func.count(Recipe.id).label("recipe_count")
        )
        .join(Recipe, Recipe.category_id == Category.id)
        .where(base_filter)
        .group_by(Category.id, Category.name, Category.slug)
        .order_by(desc("recipe_count"))
    )
    category_result = await db.execute(category_stmt)
    category_distribution = [
        {
            "categoryId": str(row.id),
            "categoryName": row.name,
            "categorySlug": row.slug,
            "recipeCount": row.recipe_count,
        }
        for row in category_result.all()
    ]

    # 4. Difficulty distribution
    difficulty_labels = {
        RecipeDifficulty.Easy.value: "Dễ",
        RecipeDifficulty.Medium.value: "Trung bình",
        RecipeDifficulty.Hard.value: "Khó",
        RecipeDifficulty.Expert.value: "Chuyên gia",
    }
    
    difficulty_stmt = (
        select(Recipe.difficulty, func.count(Recipe.id))
        .where(base_filter)
        .group_by(Recipe.difficulty)
    )
    difficulty_result = await db.execute(difficulty_stmt)
    difficulty_distribution = [
        {
            "difficulty": row[0],
            "difficultyLabel": difficulty_labels.get(row[0], "Không xác định"),
            "count": row[1],
        }
        for row in difficulty_result.all()
    ]

    return DashboardStatsDto(
        totalRecipes=total_recipes,
        publishedCount=published_count,
        draftCount=draft_count,
        archivedCount=archived_count,
        recentRecipes=recent_recipes_dto,
        categoryDistribution=category_distribution,
        difficultyDistribution=difficulty_distribution,
    )
