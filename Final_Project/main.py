from lib.models.database import create_tables
from lib.cli import main_menu

def main()
    print("🚀 Welcome to the Asset Management System...")
    create_tables()  # Ensure tables are created before starting the CLI
    main_menu()  # Start the main CLI menu

if __name__ == "__main__":
    main()  # Run the main function when the script is executed 
# This ensures that the database is set up and the CLI is launched correctly.