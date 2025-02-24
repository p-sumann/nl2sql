import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture
def test_db():
    # Create SQLite in-memory database for testing
    engine = create_engine('sqlite:///:memory:', echo=False)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return engine, SessionLocal


def test_create_db_connection(test_db):
    engine, SessionLocal = test_db
    
    # Create a test session
    test_session = SessionLocal()
    
    # Basic assertions
    assert engine is not None
    assert SessionLocal is not None
    
    # Clean up
    test_session.close()
