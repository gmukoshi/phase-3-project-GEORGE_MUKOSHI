import sqlite3
import os

# --- Database setup ---
DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "db",
    "database.db"
)
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

CONN = sqlite3.connect(DB_PATH)
CURSOR = CONN.cursor()


def create_tables():
    """Create tables for employees and assets."""
    CURSOR.execute("PRAGMA foreign_keys = ON;")

    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL
        );
    """)

    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_type TEXT NOT NULL,
            serial_number TEXT UNIQUE,
            boot_size TEXT,
            overall_size TEXT,
            employee_id INTEGER,
            notes TEXT,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE SET NULL
        );
    """)

    CONN.commit()
