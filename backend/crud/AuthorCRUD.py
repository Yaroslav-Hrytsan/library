from sqlalchemy.orm import Session
from backend.models import Author

def create_author(db: Session, new_author: str):
    author = Author(name=new_author)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

def get_authors(db: Session):
    return db.query(Author).all()

def update_author(db: Session, author_id: int, new_name: str):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        return None
    author.name = new_name
    db.commit()
    db.refresh(author)
    return author

def delete_author(db: Session, author_id: int):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        return None
    db.delete(author)
    db.commit()
    return author
