import sqlite3
from pathlib import Path


# Find the project's root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Set the database file location
DATABASE_PATH = BASE_DIR / "data" / "placement.db"


def create_connection():
    """Create and return a connection to the database."""
    connection = sqlite3.connect(DATABASE_PATH)
    return connection


def create_students_table():
    """Create the students table if it does not exist."""

    connection = create_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            college TEXT NOT NULL,
            degree TEXT NOT NULL,
            graduation_year INTEGER NOT NULL
        )
    """)

    connection.commit()
    connection.close()

    print("Database and students table are ready!")