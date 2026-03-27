from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    year: int

class BookCreate(BookBase):
    author_id: int

class BookUpdate(BaseModel):
    title: str| None = None
    year: int | None = None
    author_id: int | None = None

class BookOut(BookBase):
    id: int
    author_id: int
    class Config:
        from_attributes = True