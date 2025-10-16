from lib.models.database import CONN, CURSOR

class Employee:
    def __init__(self, name, department, id=None):
        self.id = id
        self.name = name
        self.department = department

    def save(self):
        """Insert a new employee record."""
        CURSOR.execute("""
            INSERT INTO employees (name, department)
            VALUES (?, ?)
        """, (self.name, self.department))
        CONN.commit()
        self.id = CURSOR.lastrowid
        print(f"✅ Employee '{self.name}' added successfully (ID: {self.id})")

    def update(self):
        """Update employee details."""
        CURSOR.execute("""
            UPDATE employees
            SET name=?, department=?
            WHERE id=?
        """, (self.name, self.department, self.id))
        CONN.commit()
        print(f"📝 Employee ID {self.id} updated successfully.")

    def delete(self):
        """Delete employee record."""
        CURSOR.execute("DELETE FROM employees WHERE id=?", (self.id,))
        CONN.commit()
        print(f"🗑️ Employee ID {self.id} deleted successfully.")

    @classmethod
    def all(cls):
        """Return all employees."""
        rows = CURSOR.execute("SELECT * FROM employees").fetchall()
        return [cls(row[1], row[2], id=row[0]) for row in rows]

    @classmethod
    def find_by_id(cls, employee_id):
        """Find employee by ID."""
        row = CURSOR.execute("SELECT * FROM employees WHERE id=?", (employee_id,)).fetchone()
        return cls(row[1], row[2], id=row[0]) if row else None

    def get_assets(self):
        """Return all assets assigned to this employee."""
        from lib.models.assets import Asset
        rows = CURSOR.execute("SELECT * FROM assets WHERE employee_id=?", (self.id,)).fetchall()
        return [Asset(*row[1:], id=row[0]) for row in rows]