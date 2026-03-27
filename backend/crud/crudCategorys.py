from sqlalchemy.orm import Session
from backend.schemas import CategoryCreate
from backend.models import Category

def get_categories(db: Session):
    return db.query(Category).all()

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
