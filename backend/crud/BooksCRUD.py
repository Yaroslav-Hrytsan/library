from sqlalchemy.orm import Session
from backend.schemas import BookCreate, BookUpdate
from backend.models import Book

def create_book(db: Session, book: BookCreate):
    new_book = Book(
        title=book.title, 
        year=book.year,
        author_id=book.author_id,
        category_id=book.category_id)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# category_id: int | None = None
def get_books(db: Session, author_id: int | None=None,  year: int | None = None, category_id: int | None = None):
    books = db.query(Book)
    if author_id:
        books = books.filter(Book.author_id == author_id)
    if category_id:
        books = books.filter(Book.category_id == category_id)
    if year:
        books = books.filter(Book.year == year)
    return books.all()

def update_book(db: Session, book_id: int, book: BookUpdate):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        return None
    update_data = book.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        return None
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}

# def search_books(db: Session, search_value: str):
#     return db.query(Book).join(Author).join(Category).filter(
#         (Book.title.ilike(f"%{search_value}%")) |
#         (Book.year.ilike(f"%{search_value}%")) |
#         (Author.name.ilike(f"%{search_value}%")) |
#         (Category.name.ilike(f"%{search_value}%"))
#     ).all()