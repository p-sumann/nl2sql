import os
import sys

from sqlalchemy import (
    Boolean,
    Column,
    Float,
    Integer,
    String,
)
from sqlalchemy.orm import declarative_base

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from database import create_db_connection

from src.config import config

Base = declarative_base()


# flights table
class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True)
    YEAR = Column(Integer)
    MONTH = Column(Integer)
    DAY = Column(Integer)
    DAY_OF_WEEK = Column(Integer)
    AIRLINE = Column(String)
    FLIGHT_NUMBER = Column(Integer)
    TAIL_NUMBER = Column(String)
    ORIGIN_AIRPORT = Column(String)
    DESTINATION_AIRPORT = Column(String)
    SCHEDULED_DEPARTURE = Column(Integer)
    DEPARTURE_TIME = Column(Integer)
    DEPARTURE_DELAY = Column(Float)
    TAXI_OUT = Column(Float)
    WHEELS_OFF = Column(Integer)
    SCHEDULED_TIME = Column(Float)
    ELAPSED_TIME = Column(Float)
    AIR_TIME = Column(Float)
    DISTANCE = Column(Integer)
    WHEELS_ON = Column(Integer)
    TAXI_IN = Column(Float)
    SCHEDULED_ARRIVAL = Column(Integer)
    ARRIVAL_TIME = Column(Integer)
    ARRIVAL_DELAY = Column(Float)
    DIVERTED = Column(Boolean)
    CANCELLED = Column(Boolean)
    CANCELLATION_REASON = Column(String)
    AIR_SYSTEM_DELAY = Column(Float)
    SECURITY_DELAY = Column(Float)
    AIRLINE_DELAY = Column(Float)
    LATE_AIRCRAFT_DELAY = Column(Float)
    WEATHER_DELAY = Column(Float)


# airports table
class Airport(Base):
    __tablename__ = "airports"

    IATA_CODE = Column(String, primary_key=True)
    AIRPORT = Column(String)
    CITY = Column(String)
    STATE = Column(String)
    COUNTRY = Column(String)
    LATITUDE = Column(Float)
    LONGITUDE = Column(Float)


# airlines table
class Airline(Base):
    __tablename__ = "airlines"

    IATA_CODE = Column(String, primary_key=True)
    AIRLINE = Column(String)


def create_tables(password: str):
    """Drops all existing tables and creates new ones in the database."""
    engine, _ = create_db_connection(password)
    Base.metadata.drop_all(bind=engine)  # Drop all existing tables
    Base.metadata.create_all(bind=engine)  # Create new tables


if __name__ == "__main__":
    create_tables(config.DB_PASS)
    print("Tables created!!!")
