from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.db_models import Base

DATABASE_URL = "sqlite:///./users.db"

# Create the engine and session maker
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables if they don't exist
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
