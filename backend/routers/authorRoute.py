from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session
from backend.crud.AuthorCRUD import delete_author
from backend.schemas import AuthorBase, AuthorCreate, AuthorOut
from backend.crud import get_authors, create_author, update_author
from backend.database import get_db

router = APIRouter(
    prefix="/authors",
    tags=["authors"]
)


@router.post("/", response_model=AuthorOut)
def create_author_route(name: str, db: Session = Depends(get_db)):
    return create_author(db, name)

@router.get("/", response_model=list[AuthorOut])
def read_authors_route(db: Session = Depends(get_db)):
    author = get_authors(db)
    if author is None:
        raise HTTPException(status_code=404, detail="Authors not found")
    return author

@router.put("/{author_id}", response_model=AuthorOut)
def update_author_route(author_id: int, name: str, db: Session = Depends(get_db)):
    author = update_author(db, author_id, name)
    if author is None:
        return HTTPException(status_code=404, detail="Author not found")
    return author

@router.delete("/{author_id}", response_model=AuthorOut)
def delete_author_route(author_id: int, db: Session = Depends(get_db)):
    author = delete_author(db, author_id)
    if author is None:
        return HTTPException(status_code=404, detail="Author not found")
    return author