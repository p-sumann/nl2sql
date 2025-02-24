import logging
from typing import Dict

import pandas as pd
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

from src.config import config
from src.db.database import create_db_connection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DatabaseConnector:
    def __init__(self):
        self.engine, self.SessionLocal = create_db_connection(config.DB_PASS)

    def execute_query(self, query: str) -> Dict:
        """Executes the given SQL query and returns the results as a list of dictionaries."""
        try:
            df_result = pd.read_sql_query(query, self.engine)
            df_result = self._parse_nan_values(df_result)
            df_result = self._parse_numeric_values(df_result)
            return df_result.to_dict(orient="records")
        except SQLAlchemyError as e:
            logger.error(f"Database error: {e}")
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
        except Exception:
            logger.exception("Unexpected error during query execution")
            raise HTTPException(status_code=500, detail="Error executing query.")

    def _parse_nan_values(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """Replaces NaN values in the DataFrame with empty strings."""
        return dataframe.fillna("")

    def _parse_numeric_values(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """Rounds numeric values in the DataFrame to 2 decimal places."""
        for column in dataframe.select_dtypes(include=["number"]).columns:
            dataframe[column] = dataframe[column].round(2)
        return dataframe
