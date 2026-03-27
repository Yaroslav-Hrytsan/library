from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# database.py'
DATABASE_URL = "sqlite:///./library.db"

# з'єднання з базою даних
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# створення сесії
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# створення базового класу
Base = declarative_base()

# отримання бд сесії
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()