from lib.models.database import CONN, CURSOR
import sqlite3

class Asset:
    def __init__(self, asset_type, serial_number, employee_id=None, notes=None, id=None):
        self.id = id
        self.asset_type = asset_type
        self.serial_number = serial_number
        self.employee_id = employee_id
        self.notes = notes

    def save(self):
        """Insert or update asset record."""
        if not self.asset_type or not self.serial_number:
            raise ValueError("Asset type and serial number required.")

        try:
            if self.id:
                CURSOR.execute(
                    "UPDATE assets SET asset_type=?, serial_number=?, employee_id=?, notes=? WHERE id=?",
                    (self.asset_type, self.serial_number, self.employee_id, self.notes, self.id)
                )
            else:
                CURSOR.execute(
                    "INSERT INTO assets (asset_type, serial_number, employee_id, notes) VALUES (?, ?, ?, ?)",
                    (self.asset_type, self.serial_number, self.employee_id, self.notes)
                )
                self.id = CURSOR.lastrowid
            CONN.commit()
        except sqlite3.IntegrityError:
            print("❌ Serial number already exists — must be unique.")
        return self

    def delete(self):
        CURSOR.execute("DELETE FROM assets WHERE id=?", (self.id,))
        CONN.commit()

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM assets WHERE id=?", (id,))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[0]) if row else None

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM assets")
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[4], row[0]) for row in rows]

    @classmethod
    def find_by_employee(cls, employee_id):
        CURSOR.execute("SELECT * FROM assets WHERE employee_id=?", (employee_id,))
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[4], row[0]) for row in rows]

    def __repr__(self):
        return f"<Asset {self.id}: {self.asset_type} ({self.serial_number})>"
