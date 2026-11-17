from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field


class UserListItemDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

    id: str
    fullName: str
    userName: str
    email: str
    avatarUrl: Optional[str] = None
    bio: Optional[str] = None
    role: str = "Author"
    isActive: bool = True
    emailConfirmed: bool = False
    recipeCount: int = 0
    createdAt: datetime


class UserRoleUpdateRequest(BaseModel):
    role: str = Field(..., pattern=r"^(Admin|Author|User)$", json_schema_extra={"example": "Author"})


class UserStatusUpdateRequest(BaseModel):
    isActive: bool = Field(..., json_schema_extra={"example": True})
