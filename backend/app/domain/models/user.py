import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Boolean, Integer, DateTime, Text
from sqlalchemy.orm import relationship
from app.core.database import Base


class User(Base):
    """
    SRS Chapter 7.7: ApplicationUser
    Table name: "users" (or "AspNetUsers")
    """
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    full_name = Column(String(100), nullable=False)
    user_name = Column(String(100), unique=True, nullable=False, index=True)
    email = Column(String(256), unique=True, nullable=False, index=True)
    password_hash = Column(String(500), nullable=True)
    avatar_url = Column(String(500), nullable=True)
    bio = Column(Text, nullable=True)
    role = Column(String(50), default="Author", nullable=False)  # "Author", "Admin"
    is_active = Column(Boolean, default=True, nullable=False)
    email_confirmed = Column(Boolean, default=False, nullable=False)
    access_failed_count = Column(Integer, default=0, nullable=False)
    lockout_end = Column(DateTime(timezone=True), nullable=True)
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

    # Relationships
    refresh_tokens = relationship("RefreshToken", back_populates="user", cascade="all, delete-orphan")
    recipes = relationship("Recipe", back_populates="author", cascade="all, delete-orphan")

    def is_locked_out(self) -> bool:
        if self.lockout_end is None:
            return False
        return self.lockout_end > datetime.now(timezone.utc)
