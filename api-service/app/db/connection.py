from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)   # creating db session

def get_db():
    db = SessionLocal()
    try:
        yield db     # gives session to path operations(i.e. API handler)
    finally:
        db.close()