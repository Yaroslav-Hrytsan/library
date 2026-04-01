from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session
from backend.models.BookModel import Book
from backend.schemas import BookCreate, BookUpdate, BookOut
from backend.crud import get_books, create_book, update_book, delete_book
from backend.database import get_db

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

@router.post("/", response_model=BookOut)
def create_book_route(title: str, year: int, author_id: int, category_id, db: Session = Depends(get_db)):
    return create_book(db, title, year, author_id, category_id, )

@router.get("/", response_model=list[BookOut])
def read_books_route(db: Session = Depends(get_db), author_id: int | None = None, category_id: str | None = None, year: int | None = None):
    books= get_books(db, author_id, category_id, year)
    if not books:
        return HTTPException(status_code=404, detail="Book not found")
    return books

@router.put("/{book_id}", response_model=BookOut)
def update_book_route(book_id:int, title: str | None = None, year: int | None = None, author_id: int | None = None, category_id: str | None = None, db: Session=Depends(get_db)):
    book = update_book(db, book_id, category_id, author_id, year, title)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.delete("/{book_id}", response_model=BookOut)
def delete_book_route(book_id: int, db: Session = Depends(get_db)):
    book = delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


# @router.get("/search", response_model=list[BookOut])
# def search_books_route(search_value: str, db: Session = Depends(get_db)):
#     books = search_books(db, search_value)
#     if not books:
#         raise HTTPException(status_code=404, detail="Book not found")
#     return books
