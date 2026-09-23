from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from app.core.config import settings

# Database URLs
async_url = settings.get_database_url()
sync_url = settings.get_sync_database_url()

# Async Engine and Session
async_engine = create_async_engine(
    async_url,
    echo=(settings.ENVIRONMENT == "development"),
    future=True,
    pool_size=20,
    max_overflow=10,
)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

# Sync Engine (for migrations, scripts and synchronous operations)
sync_engine = create_engine(
    sync_url,
    echo=(settings.ENVIRONMENT == "development"),
    pool_size=10,
    max_overflow=5,
)
SyncSessionLocal = sessionmaker(bind=sync_engine, autocommit=False, autoflush=False)

Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency that provides an async database session."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
