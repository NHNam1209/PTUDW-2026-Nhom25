from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.domain.models.base import BaseEntity


class RecipeImage(BaseEntity):
    """
    SRS Chapter 7.5: RecipeImage
    Stores URLs of images hosted on MinIO (original, medium, thumbnail).
    """
    __tablename__ = "recipe_images"

    recipe_id = Column(
        UUID(as_uuid=True),
        ForeignKey("recipes.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    original_url = Column(String(500), nullable=False)
    medium_url = Column(String(500), nullable=True)
    thumbnail_url = Column(String(500), nullable=True)
    alt_text = Column(String(200), nullable=True)
    is_primary = Column(Boolean, default=False, nullable=False)
    order_index = Column(Integer, default=0, nullable=False)

    # Relationships
    recipe = relationship("Recipe", back_populates="images")
