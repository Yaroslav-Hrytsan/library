from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    year: int
    author_id: int
    # category_id: str 

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    title: str| None = None
    year: int | None = None
    author_id: int | None = None
    # category_id: str | None = None

class BookOut(BookBase):
    id: int
    class Config:
        from_attributes = True