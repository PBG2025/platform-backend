import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Session
from sqlalchemy.orm import sessionmaker, SessionLocal
from fastapi import Depends


# Load from .env in local dev; safe to run in production too (ignored if no file)
load_dotenv()

# Get environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

# Validate
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set")

# get_db() function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# Create database engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

