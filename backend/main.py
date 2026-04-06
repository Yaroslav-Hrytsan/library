
from fastapi import FastAPI
from backend.routers import AuthorRoute, BooksRoute, CategoryRoute 
from fastapi.middleware.cors import CORSMiddleware
from backend.database import Base, engine


app = FastAPI(
    title="Library API",
    description="API для управління cd",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # або ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(AuthorRoute.router)
app.include_router(BooksRoute.router)
app.include_router(CategoryRoute.router)
