from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str
    id: int

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int
    class Config:
        from_attributes = True

