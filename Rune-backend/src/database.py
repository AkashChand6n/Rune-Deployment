# src/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config  # Importing your MySQL DB config

# Use the MySQL connection URL from config.py
SQLALCHEMY_DATABASE_URL = Config.SQLALCHEMY_DATABASE_URI

# Create the engine (no need for connect_args with MySQL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
