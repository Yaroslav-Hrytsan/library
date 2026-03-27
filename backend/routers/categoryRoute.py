# routers/categoryRoute.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.schemas import CategoryOut, CategoryCreate
from backend.crud import create_category, get_categories
from backend.database import get_db

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@router.get("/", response_model=list[CategoryOut])
def read_categories(db: Session = Depends(get_db)):
    return get_categories(db)

@router.post("/", response_model=CategoryOut)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)
