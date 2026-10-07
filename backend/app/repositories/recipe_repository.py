from typing import Optional, List, Tuple
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_
from sqlalchemy.orm import selectinload
from app.domain.models.recipe import Recipe
from app.repositories.base import BaseRepository


class RecipeRepository(BaseRepository[Recipe]):
    """Repository handling persistence operations for Recipe aggregate."""
    def __init__(self, session: AsyncSession):
        super().__init__(session, Recipe)

    async def get_by_slug_with_details(self, slug: str) -> Optional[Recipe]:
        stmt = (
            select(Recipe)
            .where(Recipe.slug == slug, Recipe.is_deleted == False)
            .options(
                selectinload(Recipe.ingredients),
                selectinload(Recipe.steps),
                selectinload(Recipe.images),
                selectinload(Recipe.category),
                selectinload(Recipe.author),
            )
        )
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def get_by_id_with_details(self, recipe_id: UUID) -> Optional[Recipe]:
        stmt = (
            select(Recipe)
            .where(Recipe.id == recipe_id, Recipe.is_deleted == False)
            .options(
                selectinload(Recipe.ingredients),
                selectinload(Recipe.steps),
                selectinload(Recipe.images),
                selectinload(Recipe.category),
                selectinload(Recipe.author),
            )
        )
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def list_published(
        self,
        category_id: Optional[UUID] = None,
        difficulty: Optional[int] = None,
        skip: int = 0,
        limit: int = 12
    ) -> Tuple[List[Recipe], int]:
        filters = [Recipe.is_deleted == False, Recipe.status == 1]
        if category_id:
            filters.append(Recipe.category_id == category_id)
        if difficulty:
            filters.append(Recipe.difficulty == difficulty)

        # Count total
        count_stmt = select(func.count(Recipe.id)).where(and_(*filters))
        total_res = await self.session.execute(count_stmt)
        total = total_res.scalar() or 0

        # Query items
        stmt = (
            select(Recipe)
            .where(and_(*filters))
            .options(
                selectinload(Recipe.images),
                selectinload(Recipe.category),
                selectinload(Recipe.author),
            )
            .order_by(Recipe.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        items_res = await self.session.execute(stmt)
        items = list(items_res.scalars().all())

        return items, total
