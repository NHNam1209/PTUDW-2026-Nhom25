from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import AsyncSessionLocal
from app.repositories.user_repository import UserRepository
from app.repositories.recipe_repository import RecipeRepository


class IUnitOfWork:
    """Interface defining the Unit of Work pattern contract."""
    users: UserRepository
    recipes: RecipeRepository

    async def __aenter__(self):
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError

    async def commit(self):
        raise NotImplementedError

    async def rollback(self):
        raise NotImplementedError


class UnitOfWork(IUnitOfWork):
    """
    SQLAlchemy Unit of Work implementation.
    Manages atomic transaction boundary across multiple repositories.
    """
    def __init__(self, session_factory=AsyncSessionLocal):
        self.session_factory = session_factory
        self.session: Optional[AsyncSession] = None

    async def __aenter__(self):
        self.session = self.session_factory()
        self.users = UserRepository(self.session)
        self.recipes = RecipeRepository(self.session)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            await self.rollback()
        else:
            await self.commit()
        await self.session.close()

    async def commit(self):
        if self.session:
            await self.session.commit()

    async def rollback(self):
        if self.session:
            await self.session.rollback()


async def get_uow():
    """FastAPI Dependency for Unit of Work."""
    async with UnitOfWork() as uow:
        yield uow
