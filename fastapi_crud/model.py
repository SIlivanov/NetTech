from typing import List
from pydantic import BaseModel


# Полная модель задачи
class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Пример задачи от разработчика(Иванов КА)"
            }
        }


# Модель для обновления/создания без ID
class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Прочитать главу книги по FastAPI"
            }
        }


# Модель ответа (скрывает ID в ответе списка)
class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {"item": "Задача 1"},
                    {"item": "Задача 2"}
                ]
            }
        }
