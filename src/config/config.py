import os

from dotenv import load_dotenv

load_dotenv()

# Environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DB_PASS = os.getenv("PASS")
DB_NAME = os.getenv("DATABASE")
DB_USER = os.getenv("USER")
DB_HOST = os.getenv("HOST")
DB_CLIENT = os.getenv("DATABASE_CLIENT")
DB_PORT = os.getenv("PORT")
