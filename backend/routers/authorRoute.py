from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from backend.schemas import AuthorBase, AuthorCreate, AuthorOut
from backend.crud import get_authors, create_author
from backend.database import get_db

router = APIRouter(
    prefix="/authors",
    tags=["authors"]
)

@router.get("/", response_model=list[AuthorBase])
def read_authors(db: Session = Depends(get_db)):
    return get_authors(db)

@router.post("/", response_model=AuthorOut)
def create_new_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return create_author(db, author)
