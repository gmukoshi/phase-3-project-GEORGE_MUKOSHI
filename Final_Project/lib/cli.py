from lib.models.employee import Employee
from lib.models.assets import Asset
from lib.models.database import CURSOR

def main_menu():
    while True:
        print("\n🏢 Main Menu")
        print("1. Manage Employees")
        print("2. Manage Assets")
        print("3. Generate Reports")
        print("4. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            employee_menu()
        elif choice == "2":
            asset_menu()
        elif choice == "3":
            generate_reports()
        elif choice == "4":
            print("👋 Exiting system...")
            break
        else:
            print("❌ Invalid choice. Try again.")


# ---------- EMPLOYEE MANAGEMENT ----------
def employee_menu():
    while True:
        print("\n👩‍💼 Employee Management")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Delete Employee")
        print("4. View Employee Assets")
        print("5. Back")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter employee name: ")
            dept = input("Enter department: ")
            Employee(name, dept).save()
        elif choice == "2":
            for emp in Employee.all():
                print(f"ID: {emp.id}, Name: {emp.name}, Dept: {emp.department}")
        elif choice == "3":
            eid = input("Enter Employee ID to delete: ")
            emp = Employee.find_by_id(eid)
            if emp: emp.delete()
            else: print("Employee not found.")
        elif choice == "4":
            eid = input("Enter Employee ID: ")
            emp = Employee.find_by_id(eid)
            if emp:
                assets = emp.get_assets()
                if assets:
                    for a in assets:
                        print(f" - {a.asset_type} ({a.serial_number or a.boot_size or a.overall_size})")
                else:
                    print("No assets assigned.")
            else:
                print("Employee not found.")
        elif choice == "5":
            break


# ---------- ASSET MANAGEMENT ----------
def asset_menu():
    while True:
        print("\n💻 Asset Management")
        print("1. Add Asset")
        print("2. View All Assets")
        print("3. Delete Asset")
        print("4. Back")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_asset()
        elif choice == "2":
            for a in Asset.all():
                print(f"ID: {a.id}, Type: {a.asset_type}, Serial: {a.serial_number or '-'}, "
                      f"Boot Size: {a.boot_size or '-'}, Overall Size: {a.overall_size or '-'}, "
                      f"Employee ID: {a.employee_id or '-'}")
        elif choice == "3":
            aid = input("Enter Asset ID to delete: ")
            asset = Asset.find_by_id(aid)
            if asset: asset.delete()
            else: print("Asset not found.")
        elif choice == "4":
            break


def add_asset():
    asset_type = input("Enter asset type (Laptop / Safety Boot / Overall / Toolkit): ").title()
    serial_number = boot_size = overall_size = None

    if asset_type.lower() in ["laptop", "toolkit"]:
        serial_number = input("Enter serial number: ")
    elif asset_type.lower() == "safety boot":
        boot_size = input("Enter boot size (e.g. 42): ")
    elif asset_type.lower() == "overall":
        overall_size = input("Enter overall size (e.g. M, L, XL): ")

    emp_id = input("Assign to Employee ID (optional): ") or None
    notes = input("Any notes? (optional): ")

    Asset(asset_type, serial_number, boot_size, overall_size, emp_id, notes).save()


# ---------- REPORTS ----------
def generate_reports():
    print("\n📊 Asset Summary by Type:")
    rows = CURSOR.execute("SELECT asset_type, COUNT(*) FROM assets GROUP BY asset_type").fetchall()
    for t, c in rows:
        print(f" - {t}: {c} item(s)")

    print("\n📊 Assets per Employee:")
    rows = CURSOR.execute("""
        SELECT e.name, COUNT(a.id)
        FROM employees e
        LEFT JOIN assets a ON e.id = a.employee_id
        GROUP BY e.id
    """).fetchall()
    for name, count in rows:
        print(f" - {name}: {count} asset(s)")
