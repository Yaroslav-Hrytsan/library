from fastapi import FastAPI
from backend.database import Base, engine
from backend.routers import authorRoute, booksRoute, categoryRoute 

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Library API",
    description="API для управління бібліотекою",
    version="1.0.0",
)
app.include_router(authorRoute.router)
app.include_router(booksRoute.router)
app.include_router(categoryRoute.router)
