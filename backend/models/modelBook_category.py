from sqlalchemy import Table, Column, Integer, ForeignKey
from backend.database import Base

book_category = Table(
    "book_category",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id")),
    Column("category_id", Integer, ForeignKey("categories.id"))
)