from typing import Any, Dict, Generic, List, Optional, TypeVar
from pydantic import BaseModel, Field

T = TypeVar("T")


class PagedMeta(BaseModel):
    page: int = Field(..., json_schema_extra={"example": 1})
    pageSize: int = Field(..., json_schema_extra={"example": 12})
    total: int = Field(..., json_schema_extra={"example": 100})
    totalPages: int = Field(..., json_schema_extra={"example": 9})
    hasNextPage: bool = Field(..., json_schema_extra={"example": True})
    hasPreviousPage: bool = Field(..., json_schema_extra={"example": False})


class PagedResult(BaseModel, Generic[T]):
    items: List[T]
    meta: PagedMeta


class ProblemDetails(BaseModel):
    type: str = Field(..., json_schema_extra={"example": "VALIDATION_ERROR"})
    title: str = Field(..., json_schema_extra={"example": "Unprocessable Entity"})
    status: int = Field(..., json_schema_extra={"example": 422})
    detail: str = Field(..., json_schema_extra={"example": "Dữ liệu yêu cầu không hợp lệ."})
    errors: Dict[str, List[str]] = Field(default_factory=dict)
