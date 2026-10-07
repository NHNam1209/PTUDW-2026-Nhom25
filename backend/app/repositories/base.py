from typing import Generic, TypeVar, Type, Optional, List, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, func
from app.domain.models.base import BaseEntity

T = TypeVar("T", bound=BaseEntity)


class IRepository(Generic[T]):
    """Generic Repository Interface defining contract for data access operations."""
    async def get_by_id(self, id: Any) -> Optional[T]:
        raise NotImplementedError

    async def list_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        raise NotImplementedError

    async def add(self, entity: T) -> T:
        raise NotImplementedError

    async def update(self, entity: T) -> T:
        raise NotImplementedError

    async def delete(self, entity: T) -> None:
        raise NotImplementedError

    async def count(self) -> int:
        raise NotImplementedError


class BaseRepository(IRepository[T], Generic[T]):
    """Base generic repository implementation using SQLAlchemy 2.0 AsyncSession."""
    def __init__(self, session: AsyncSession, model_cls: Type[T]):
        self.session = session
        self.model_cls = model_cls

    async def get_by_id(self, id: Any) -> Optional[T]:
        stmt = select(self.model_cls).where(self.model_cls.id == id, self.model_cls.is_deleted == False)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def list_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        stmt = (
            select(self.model_cls)
            .where(self.model_cls.is_deleted == False)
            .offset(skip)
            .limit(limit)
        )
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def add(self, entity: T) -> T:
        self.session.add(entity)
        await self.session.flush()
        return entity

    async def update(self, entity: T) -> T:
        # Increment row_version for optimistic concurrency
        if hasattr(entity, "row_version"):
            entity.row_version += 1
        await self.session.flush()
        return entity

    async def delete(self, entity: T) -> None:
        # Soft delete
        if hasattr(entity, "is_deleted"):
            entity.is_deleted = True
            await self.session.flush()
        else:
            await self.session.delete(entity)

    async def count(self) -> int:
        stmt = select(func.count(self.model_cls.id)).where(self.model_cls.is_deleted == False)
        result = await self.session.execute(stmt)
        return result.scalar() or 0
