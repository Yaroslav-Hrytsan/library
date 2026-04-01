from fastapi import FastAPI
from backend.database import Base, engine
from backend.routers import AuthorRoute, BooksRoute, CategoryRoute 

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Library API",
    description="API для управління бібліотекою",
    version="1.0.0",
)
app.include_router(AuthorRoute.router)
app.include_router(BooksRoute.router)
app.include_router(CategoryRoute.router)
