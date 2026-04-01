# routers/categoryRoute.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.crud.CategoryCRUD import update_category
from backend.schemas import CategoryOut, CategoryCreate, CategoryUpdate
from backend.crud import create_category, get_categories
from backend.database import get_db

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@router.post("/", response_model=CategoryOut)
def create_category_router(new_category: str, db: Session = Depends(get_db)):
    return create_category(db, new_category)

@router.get("/", response_model=list[CategoryOut])
def read_categories_router(db: Session = Depends(get_db)):
    categories = get_categories(db)
    if not categories:
        raise HTTPException(status_code=404, detail="Categories not found")
    return categories

@router.put("/{category_id}", response_model=CategoryOut)
def update_category_router(category_id: int, name: str, db: Session = Depends(get_db)):
    category = update_category(db, category_id, name)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = delete_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category