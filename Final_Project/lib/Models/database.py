import sqlite3
import os

# Database file path
DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "db",
    "database.db"
)

# Ensure the db/ folder exists
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Shared connection and cursor
CONN = sqlite3.connect(DB_PATH)
CURSOR = CONN.cursor()

def create_tables():
    """Create all required tables."""
    CURSOR.execute("PRAGMA foreign_keys = ON;")

    # Employee Table
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL
        );
    """)

    # Asset Table
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_type TEXT NOT NULL,
            serial_number TEXT NOT NULL UNIQUE,
            employee_id INTEGER,
            notes TEXT,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE SET NULL
        );
    """)

    CONN.commit()
