from lib.models.database import CONN, CURSOR

class Employee:
    def __init__(self, name, department, id=None):
        self.id = id
        self.name = name
        self.department = department

    def save(self):
        """Insert or update employee record."""
        if not self.name or not self.department:
            raise ValueError("Name and Department are required.")
        if self.id:
            CURSOR.execute(
                "UPDATE employees SET name=?, department=? WHERE id=?",
                (self.name, self.department, self.id)
            )
        else:
            CURSOR.execute(
                "INSERT INTO employees (name, department) VALUES (?, ?)",
                (self.name, self.department)
            )
            self.id = CURSOR.lastrowid
        CONN.commit()
        return self

    def delete(self):
        CURSOR.execute("DELETE FROM employees WHERE id=?", (self.id,))
        CONN.commit()

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM employees WHERE id=?", (id,))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[0]) if row else None

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM employees")
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[0]) for row in rows]

    def get_assets(self):
        from lib.models.assets import Asset
        return Asset.find_by_employee(self.id)

    def __repr__(self):
        return f"<Employee {self.id}: {self.name} ({self.department})>"
