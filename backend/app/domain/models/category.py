from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import relationship
from app.domain.models.base import BaseEntity


class Category(BaseEntity):
    """
    SRS Chapter 7.6: Category
    Categorizes recipes with SEO-friendly slugs.
    """
    __tablename__ = "categories"

    name = Column(String(100), unique=True, nullable=False, index=True)
    slug = Column(String(120), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    image_url = Column(String(500), nullable=True)
    order_index = Column(Integer, default=0, nullable=False)

    # Relationships
    recipes = relationship("Recipe", back_populates="category")
