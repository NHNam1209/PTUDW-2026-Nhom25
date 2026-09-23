from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.domain.models.base import BaseEntity


class RecipeStep(BaseEntity):
    """
    SRS Chapter 7.3: RecipeStep
    Sequential preparation steps for a recipe.
    """
    __tablename__ = "recipe_steps"

    recipe_id = Column(
        UUID(as_uuid=True),
        ForeignKey("recipes.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    step_number = Column(Integer, nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    timer_minutes = Column(Integer, nullable=True)
    image_url = Column(String(500), nullable=True)

    # Relationships
    recipe = relationship("Recipe", back_populates="steps")
