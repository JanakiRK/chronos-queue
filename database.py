import os
import psycopg2
from psycopg2.extras import RealDictCursor

# Connection details matching your docker-compose.yml
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "chronos")
DB_USER = os.getenv("DB_USER", "chronos_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "chronos_password")
DB_PORT = os.getenv("DB_PORT", "5432")

def get_db_connection():
    """Establishes a connection to PostgreSQL and returns a connection object."""
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT,
        cursor_factory=RealDictCursor
    )
    return conn