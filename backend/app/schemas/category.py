from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict


class CategoryBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, example="Món Chính")
    description: Optional[str] = Field(None, example="Các món ăn chính đậm đà hương vị")
    imageUrl: Optional[str] = Field(None, example="https://example.com/cat.jpg")
    orderIndex: int = Field(0, example=1)


class CategoryCreateDto(CategoryBase):
    pass


class CategoryUpdateDto(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    description: Optional[str] = None
    imageUrl: Optional[str] = None
    orderIndex: Optional[int] = None


class CategoryDto(CategoryBase):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

    id: UUID
    slug: str
    recipeCount: int = 0
