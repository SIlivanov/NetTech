from sqlmodel import SQLModel, Field
from typing import Optional

# Таблица пользователей в базе SQLite
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!"
            }
        }

# Схема для входа (авторизации)
class UserSignIn(SQLModel):
    email: str
    password: str