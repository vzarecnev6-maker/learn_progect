from pydantic import BaseModel, Field

# 8.    Вариант 8. Больница или поликлиника.
# Система хранения сведений о пациентах, приёмах или врачах.
# Следует выбрать одну основную сущность и реализовать CRUD.

class CreateDoctor(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    profession: str = Field(..., min_length=3, max_length=100)
    age: int = Field(..., ge=0)
    available: bool

class UpdateDoctor(BaseModel):
    name: str
    profession: str
    age: int
    available: bool

class PatchDoctor(BaseModel):
    name: str | None = None
    profession: str | None = None
    age: int | None = None
    available: bool | None = None

class ReadDoctor(BaseModel):
    id: int
    name: str
    profession: str
    age: int
    available: bool