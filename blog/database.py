from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlite3

from blog import models

# Correct database URL (remove check_same_threads from URL)
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

# Create synchronous engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal corrected typo
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
