from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict
from app.domain.enums import RecipeDifficulty, RecipeStatus


class RecipeNutritionDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

    calories: Optional[Decimal] = None
    protein: Optional[Decimal] = None
    carbohydrates: Optional[Decimal] = None
    fat: Optional[Decimal] = None
    fiber: Optional[Decimal] = None
    sodium: Optional[Decimal] = None


class RecipeStepCreateDto(BaseModel):
    title: str = Field(..., min_length=2, max_length=200, example="Sơ chế nguyên liệu")
    description: str = Field(..., min_length=5, example="Rửa sạch thịt bò và thái lát mỏng...")
    timerMinutes: Optional[int] = Field(None, ge=0, example=15)
    imageUrl: Optional[str] = None


class RecipeStepDto(RecipeStepCreateDto):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

    id: UUID
    stepNumber: int


class RecipeIngredientCreateDto(BaseModel):
    name: str = Field(..., min_length=1, max_length=200, example="Thịt bò thăn")
    quantity: Optional[Decimal] = Field(None, ge=0, example=500)
    unit: Optional[str] = Field(None, max_length=50, example="gram")
    notes: Optional[str] = Field(None, max_length=500, example="thái mỏng")
    orderIndex: int = Field(0, example=0)


class RecipeIngredientDto(RecipeIngredientCreateDto):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

    id: UUID


class RecipeImageDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

    id: UUID
    originalUrl: str
    mediumUrl: Optional[str] = None
    thumbnailUrl: Optional[str] = None
    altText: Optional[str] = None
    isPrimary: bool = False
    orderIndex: int = 0


class RecipeAuthorDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

    id: str
    fullName: str
    userName: str
    avatarUrl: Optional[str] = None


class RecipeCategorySummaryDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

    id: UUID
    name: str
    slug: str


class RecipeSummaryDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

    id: UUID
    title: str
    slug: str
    description: str
    prepTime: int
    cookTime: int
    servings: int
    difficulty: int
    status: int
    category: Optional[RecipeCategorySummaryDto] = None
    author: Optional[RecipeAuthorDto] = None
    primaryImage: Optional[RecipeImageDto] = None
    publishedAt: Optional[datetime] = None
    createdAt: datetime


class RecipeDetailDto(RecipeSummaryDto):
    instructions: str = ""
    nutrition: Optional[RecipeNutritionDto] = None
    steps: List[RecipeStepDto] = Field(default_factory=list)
    ingredients: List[RecipeIngredientDto] = Field(default_factory=list)
    images: List[RecipeImageDto] = Field(default_factory=list)
    rowVersion: int = 1


class RecipeCreateDto(BaseModel):
    title: str = Field(..., min_length=5, max_length=200, example="Phở Bò Gia Truyền")
    description: str = Field(..., min_length=10, max_length=2000, example="Cách nấu phở bò gia truyền thơm ngon nức mũi...")
    categoryId: UUID
    prepTimeMinutes: int = Field(..., gt=0, example=30)
    cookTimeMinutes: int = Field(..., ge=0, example=60)
    servings: int = Field(..., gt=0, example=4)
    difficulty: int = Field(1, ge=1, le=4, example=1)
    instructions: Optional[str] = Field("", example="Hướng dẫn tổng quan...")
    nutrition: Optional[RecipeNutritionDto] = None
    steps: Optional[List[RecipeStepCreateDto]] = None
    ingredients: Optional[List[RecipeIngredientCreateDto]] = None


class RecipeUpdateDto(BaseModel):
    title: Optional[str] = Field(None, min_length=5, max_length=200)
    description: Optional[str] = Field(None, min_length=10, max_length=2000)
    categoryId: Optional[UUID] = None
    prepTimeMinutes: Optional[int] = Field(None, gt=0)
    cookTimeMinutes: Optional[int] = Field(None, ge=0)
    servings: Optional[int] = Field(None, gt=0)
    difficulty: Optional[int] = Field(None, ge=1, le=4)
    instructions: Optional[str] = None
    nutrition: Optional[RecipeNutritionDto] = None
    rowVersion: Optional[int] = Field(None, description="Current row version for optimistic concurrency control")
