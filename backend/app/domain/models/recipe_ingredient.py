from sqlalchemy import Column, String, Integer, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.domain.models.base import BaseEntity


class RecipeIngredient(BaseEntity):
    """
    SRS Chapter 7.4: RecipeIngredient
    Ingredients required for the recipe.
    """
    __tablename__ = "recipe_ingredients"

    recipe_id = Column(
        UUID(as_uuid=True),
        ForeignKey("recipes.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    name = Column(String(200), nullable=False)
    quantity = Column(Numeric(10, 3), nullable=True)
    unit = Column(String(50), nullable=True)
    notes = Column(String(500), nullable=True)
    order_index = Column(Integer, default=0, nullable=False)

    # Relationships
    recipe = relationship("Recipe", back_populates="ingredients")
