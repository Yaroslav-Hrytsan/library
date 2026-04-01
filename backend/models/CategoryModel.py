from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.database import Base
from .BookCategoryModel import book_category

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    books = relationship("Book", secondary= book_category, back_populates="categories"
    )

