from sqlalchemy.orm import Session
from backend.schemas import BookCreate, BookUpdate
from backend.models import Book

def create_book(db: Session, title: str, author_id: int, category_id: str, year: int):
    new_book = Book(title=title, author_id=author_id, category_id=category_id, year=year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_books(db: Session, author_id: int | None=None, category_id: int | None = None, year: int | None = None):
    books = db.query(Book)
    if author_id:
        books = books.filter(Book.author_id == author_id)
    if category_id:
        books = books.filter(Book.category_id == category_id)
    if year:
        books = books.filter(Book.year == year)
    return books.all()

def update_book(db: Session, book_id: int, title: str, category_id: str, author_id: str, year: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        return None
    book.title= title
    book.year= year
    book.author_id= author_id
    book.categories= category_id
    return book

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        return None
    db.delete(book)
    db.commit()
    return book

# def search_books(db: Session, search_value: str):
#     return db.query(Book).join(Author).join(Category).filter(
#         (Book.title.ilike(f"%{search_value}%")) |
#         (Book.year.ilike(f"%{search_value}%")) |
#         (Author.name.ilike(f"%{search_value}%")) |
#         (Category.name.ilike(f"%{search_value}%"))
#     ).all()