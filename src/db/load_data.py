import os
import sys

from sqlalchemy import create_engine

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import pandas as pd

from src.config import config


def load_data():
    """Loads data from CSV files into the PostgreSQL database."""
    try:
        # Create SQLAlchemy engine
        engine = create_engine(
            f"postgresql://{config.DB_USER}:{config.DB_PASS}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
        )

        # Load airlines data
        airlines_df = pd.read_csv("data/airlines.csv")
        airlines_df.columns = airlines_df.columns.str.lower()
        airlines_df.to_sql("airlines", engine, if_exists="replace", index=False)

        # Load airports data
        airports_df = pd.read_csv("data/airports.csv")
        airports_df.columns = airports_df.columns.str.lower()
        airports_df.to_sql("airports", engine, if_exists="replace", index=False)

        # Load flights data
        flights_df = pd.read_csv("data/flights.csv")
        flights_df.columns = flights_df.columns.str.lower()
        flights_df.to_sql("flights", engine, if_exists="replace", index=False)

        print("Data loaded successfully!")

    except Exception as e:
        print(f"Error loading data: {e}")


if __name__ == "__main__":
    load_data()
