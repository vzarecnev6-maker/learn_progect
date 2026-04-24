from fastapi import FastAPI, HTTPException, status
from database import init_db
import crud
from schemas import BookCreate, BookUpdate, BookPatch

app = FastAPI(title="Books Rental API")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/books")
def read_books():
    return crud.get_all_books()

@app.get("/books/{book_id}")
def read_book(book_id: int):
    book = crud.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book

@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    book_id = crud.create_books(book.model_dump())
    return {"message": "Запись создана", "id": book_id}