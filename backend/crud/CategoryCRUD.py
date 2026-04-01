from sqlalchemy.orm import Session
from backend.models import Category

def create_category(db: Session, new_category: str):
    new_category = Category(name=new_category)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


def get_categories(db: Session):
    return db.query(Category).all()


def update_category(db:Session, category_id: str, new_name: str):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        return None
    category.name = new_name
    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, category_id: str):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        return None
    db.delete(category)
    db.commit()
    return category