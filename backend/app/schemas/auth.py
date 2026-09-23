from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class RegisterRequest(BaseModel):
    fullName: str = Field(..., min_length=2, max_length=100, example="Nguyễn Văn A")
    email: EmailStr = Field(..., example="user@example.com")
    userName: str = Field(..., min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9_-]+$", example="nguyenvana")
    password: str = Field(..., min_length=8, example="Admin@123456")


class LoginRequest(BaseModel):
    email: EmailStr = Field(..., example="user@example.com")
    password: str = Field(..., min_length=1, example="Admin@123456")


class GoogleLoginRequest(BaseModel):
    idToken: str = Field(..., example="eyJhbGciOiJSUzI1NiIs...")


class RefreshTokenRequest(BaseModel):
    refreshToken: str = Field(..., example="dGVzdF9yZWZyZXNoX3Rva2Vu")


class LogoutRequest(BaseModel):
    refreshToken: str = Field(..., example="dGVzdF9yZWZyZXNoX3Rva2Vu")


class UserProfileDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

    id: str
    fullName: str
    email: str
    userName: str
    avatarUrl: Optional[str] = None
    bio: Optional[str] = None
    roles: List[str] = Field(default_factory=lambda: ["Author"])
    emailConfirmed: bool = False
    createdAt: datetime


class UpdateProfileRequest(BaseModel):
    fullName: Optional[str] = Field(None, min_length=2, max_length=100)
    avatarUrl: Optional[str] = None
    bio: Optional[str] = None


class AuthResponseDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    accessToken: str
    refreshToken: str
    expiresIn: int = 900  # 15 minutes in seconds
    user: UserProfileDto
