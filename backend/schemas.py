from pydantic import BaseModel, Field

#1.	Вариант 1. Библиотека.
# Система учёта книг и операций с ними.
# Необходимо организовать хранение сведений о книгах и обеспечить базовые операции работы со списком.

class BookCreate(BaseModel):
    title: str = Field(..., min_length=2, max_length=100, description="Название книги")
    author: str = Field(..., min_length=2, max_length=100, description="Автор книги")
    available: bool

class BookUpdate(BaseModel):
    title: str
    author: str
    available: bool

class BookPatch(BaseModel):
    title: str | None = None
    author: str | None = None
    available: bool | None = None


class BookRead(BaseModel):
    id: int
    title: str
    author: str
    available: bool