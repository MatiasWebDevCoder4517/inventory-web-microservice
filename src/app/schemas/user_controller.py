# Standard Library
import uuid
from datetime import datetime

# External
from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    name: str
    email: str
    photo: str

    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    password: str
    passwordConfirm: str
    role: str = "default_user"
    verified: bool = False


class LoginUserSchema(BaseModel):
    email: str
    password: str


class UserResponse(UserBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
