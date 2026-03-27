from sqlalchemy.orm import Session
from backend.models import Author
from backend.schemas import AuthorCreate

def get_authors(db: Session):
    return db.query(Author).all()

def create_author(db: Session, author: AuthorCreate):
    db_author = Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

