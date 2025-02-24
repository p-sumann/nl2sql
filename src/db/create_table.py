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
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    day_of_week = Column(Integer)
    airline = Column(String)
    flight_number = Column(Integer)
    tail_number = Column(String)
    origin_airport = Column(String)
    destination_airport = Column(String)
    scheduled_departure = Column(Integer)
    departure_time = Column(Integer)
    departure_delay = Column(Float)
    taxi_out = Column(Float)
    wheels_off = Column(Integer)
    scheduled_time = Column(Float)
    elapsed_time = Column(Float)
    air_time = Column(Float)
    distance = Column(Integer)
    wheels_on = Column(Integer)
    taxi_in = Column(Float)
    scheduled_arrival = Column(Integer)
    arrival_time = Column(Integer)
    arrival_delay = Column(Float)
    diverted = Column(Boolean)
    cancelled = Column(Boolean)
    cancellation_reason = Column(String)
    air_system_delay = Column(Float)
    security_delay = Column(Float)
    airline_delay = Column(Float)
    late_aircraft_delay = Column(Float)
    weather_delay = Column(Float)


# airports table
class Airport(Base):
    __tablename__ = "airports"

    iata_code = Column(String, primary_key=True)
    airport = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)


# airlines table
class Airline(Base):
    __tablename__ = "airlines"

    iata_code = Column(String, primary_key=True)
    airline = Column(String)


def create_tables(password: str):
    """Drops all existing tables and creates new ones in the database."""
    engine, _ = create_db_connection(password)
    Base.metadata.drop_all(bind=engine)  # Drop all existing tables
    Base.metadata.create_all(bind=engine)  # Create new tables


if __name__ == "__main__":
    create_tables(config.DB_PASS)
    print("Tables created!!!")
