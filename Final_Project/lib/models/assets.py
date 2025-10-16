from lib.models.database import CONN, CURSOR
import sqlite3

class Asset:
    def __init__(self, asset_type, serial_number=None, boot_size=None, overall_size=None, employee_id=None, notes=None, id=None):
        self.id = id
        self.asset_type = asset_type
        self.serial_number = serial_number
        self.boot_size = boot_size
        self.overall_size = overall_size
        self.employee_id = employee_id
        self.notes = notes

    def save(self):
        """Insert a new asset record."""
        CURSOR.execute("""
            INSERT INTO assets (asset_type, serial_number, boot_size, overall_size, employee_id, notes)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (self.asset_type, self.serial_number, self.boot_size, self.overall_size, self.employee_id, self.notes))
        CONN.commit()
        self.id = CURSOR.lastrowid
        print(f"✅ Asset '{self.asset_type}' added successfully (ID: {self.id})")

    @classmethod
    def all(cls):
        """Return all assets."""
        rows = CURSOR.execute("SELECT * FROM assets").fetchall()
        return [cls(*row[1:], id=row[0]) for row in rows]

    @classmethod
    def find_by_id(cls, asset_id):
        """Find asset by ID."""
        row = CURSOR.execute("SELECT * FROM assets WHERE id=?", (asset_id,)).fetchone()
        return cls(*row[1:], id=row[0]) if row else None

    def delete(self):
        """Delete an asset."""
        CURSOR.execute("DELETE FROM assets WHERE id=?", (self.id,))
        CONN.commit()
        print(f"🗑️ Asset ID {self.id} deleted successfully.")
