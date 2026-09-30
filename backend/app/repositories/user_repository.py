from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.domain.models.user import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    """Repository handling persistence operations for User aggregate."""
    def __init__(self, session: AsyncSession):
        super().__init__(session, User)

    async def get_by_email(self, email: str) -> Optional[User]:
        stmt = select(User).where(User.email == email.lower().strip())
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def get_by_username(self, user_name: str) -> Optional[User]:
        stmt = select(User).where(User.user_name == user_name.lower().strip())
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def exists_by_email(self, email: str) -> bool:
        stmt = select(User.id).where(User.email == email.lower().strip())
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none() is not None

    async def exists_by_username(self, user_name: str) -> bool:
        stmt = select(User.id).where(User.user_name == user_name.lower().strip())
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none() is not None
