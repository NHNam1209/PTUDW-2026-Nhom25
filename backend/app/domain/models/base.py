import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base


class BaseEntity(Base):
    """
    SRS Chapter 7.1: BaseEntity (Abstract)
    - Id: uuid v4 primary key
    - CreatedAt: timestamptz not null
    - UpdatedAt: timestamptz nullable
    - IsDeleted: boolean not null default false (soft delete flag)
    - RowVersion: integer not null default 1 (optimistic concurrency control)
    """
    __abstract__ = True

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
    )
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    updated_at = Column(
        DateTime(timezone=True),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=True,
    )
    is_deleted = Column(
        Boolean,
        default=False,
        nullable=False,
        index=True,
    )
    row_version = Column(
        Integer,
        default=1,
        nullable=False,
    )
