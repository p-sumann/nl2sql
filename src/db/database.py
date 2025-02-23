from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import config


def create_db_connection(password: str):
    """Creates a database engine and a session factory."""
    database_url = f"{config.DB_CLIENT}://{config.DB_USER}:{password}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
    engine = create_engine(database_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return engine, SessionLocal