from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas import BookCreate, BookUpdate, BookOut
from backend.crud import get_books, create_book, update_book
from backend.database import get_db

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

@router.get("/", response_model=list[BookOut])
def read_books(db: Session = Depends(get_db)):
    return get_books(db)

@router.post("/", response_model=BookOut)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@router.put("/{book_id}", response_model=BookOut)
def update_existing_book(book_id:int, book: BookUpdate, db: Session=Depends(get_db)):
    db_book = update_book(db, book_id, book)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book