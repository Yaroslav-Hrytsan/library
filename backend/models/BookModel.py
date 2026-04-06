from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base
from .BookCategoryModel import book_category

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer)
    # зв'язок один до багатьох: 1book -> one author
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")
    
    # category_id = Column(String, ForeignKey("categories.id"))
    # categories = relationship("Category", secondary=book_category, back_populates="books"
    )