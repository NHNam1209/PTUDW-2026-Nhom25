from typing import Any, Dict, Generic, List, Optional, TypeVar
from pydantic import BaseModel, Field

T = TypeVar("T")


class PagedMeta(BaseModel):
    page: int = Field(..., example=1)
    pageSize: int = Field(..., example=12)
    total: int = Field(..., example=100)
    totalPages: int = Field(..., example=9)
    hasNextPage: bool = Field(..., example=True)
    hasPreviousPage: bool = Field(..., example=False)


class PagedResult(BaseModel, Generic[T]):
    items: List[T]
    meta: PagedMeta


class ProblemDetails(BaseModel):
    type: str = Field(..., example="VALIDATION_ERROR")
    title: str = Field(..., example="Unprocessable Entity")
    status: int = Field(..., example=422)
    detail: str = Field(..., example="Dữ liệu yêu cầu không hợp lệ.")
    errors: Dict[str, List[str]] = Field(default_factory=dict)
