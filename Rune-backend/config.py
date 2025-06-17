# config.py

import os

class Config:
    # Existing config
    CHROMA_DIR = "chroma_db"
    EMBEDDING_MODEL = "nomic-embed-text:latest"
    LLM_MODEL = "qwen:1.8b"
    ALLOWED_EXTENSIONS = {'txt', 'pdf'}
    UPLOAD_FOLDER = "knowledge_base"

    # MySQL + SQLAlchemy config
    MYSQL_USER = os.getenv("MYSQL_USER", "rune_user")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "password")
    MYSQL_DB = os.getenv("MYSQL_DB", "rune_db")
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
