from sqlalchemy import Column, String, Integer, SmallInteger, Text, DateTime, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.domain.models.base import BaseEntity
from app.domain.enums import RecipeDifficulty, RecipeStatus


class Recipe(BaseEntity):
    """
    SRS Chapter 7.2: Recipe Aggregate Root
    Central entity for culinary blog recipes.
    """
    __tablename__ = "recipes"

    title = Column(String(200), nullable=False)
    slug = Column(String(220), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=False)
    instructions = Column(Text, default="", nullable=False)
    prep_time = Column(Integer, default=0, nullable=False)
    cook_time = Column(Integer, default=0, nullable=False)
    servings = Column(Integer, default=1, nullable=False)
    difficulty = Column(SmallInteger, default=RecipeDifficulty.Easy.value, nullable=False, index=True)
    status = Column(SmallInteger, default=RecipeStatus.Draft.value, nullable=False, index=True)

    category_id = Column(
        UUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    author_id = Column(
        String(36),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    published_at = Column(DateTime(timezone=True), nullable=True, index=True)

    # Owned Entity RecipeNutrition (SRS 7.2.1)
    nutrition_calories = Column(Numeric(8, 2), nullable=True)
    nutrition_protein = Column(Numeric(8, 2), nullable=True)
    nutrition_carbohydrates = Column(Numeric(8, 2), nullable=True)
    nutrition_fat = Column(Numeric(8, 2), nullable=True)
    nutrition_fiber = Column(Numeric(8, 2), nullable=True)
    nutrition_sodium = Column(Numeric(8, 2), nullable=True)

    # Relationships
    category = relationship("Category", back_populates="recipes")
    author = relationship("User", back_populates="recipes")
    steps = relationship("RecipeStep", back_populates="recipe", cascade="all, delete-orphan", order_by="RecipeStep.step_number")
    ingredients = relationship("RecipeIngredient", back_populates="recipe", cascade="all, delete-orphan", order_by="RecipeIngredient.order_index")
    images = relationship("RecipeImage", back_populates="recipe", cascade="all, delete-orphan", order_by="RecipeImage.order_index")
