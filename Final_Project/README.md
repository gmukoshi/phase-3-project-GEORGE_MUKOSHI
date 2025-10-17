# Asset Inventory management App

## Introduction

The Asset Inventory Management App is a **menu-driven Command Line Interface (CLI)** application built in **Python** to help IT companies efficiently **track and manage company assets** (e.g., laptops, safety boots, overalls, toolkits) and the **employees** assigned to them.

The system ensures accountability by linking assets to employees and providing real-time summaries of asset allocations.This project aims to demonstrate Python Object-Oriented Programming (OOP), SQLite3 database integration,ORM-style data handling and CRUD operations.

## 📁 Project Structure

phase-3-project-GEORGE_MUKOSHI/
├── 

Final_Project/    # created a virtual enviroment
              
│
├── lib/                      
│   ├── cli.py                
│   └── models/               
│       ├── assets.py         
│       └── database.py       
│       └── employee.py       
│

├── db/                       
│   └── database.db           
│

├── main.py                   
├── README.md                  
└── .gitignore                

## Project Description

This project implements a menu-driven CLI for managing company assets and employees using a local SQLite3 database.

The app follows a modular structure:

- lib/ **Main project code**
- lib/database.py **handles database setup and connections.**
- lib/models/ **contains ORM-style Python classes (Employee, Asset) that manage CRUD operations.**
- lib/cli.py **provides an interactive user interface for asset and employee management.**
- main.py **acts as the entry point, ensuring the database is initialized before the program starts.**
- README.md **Project overview and setup guide**
- gitignore **Files/folders Git should ignore**
- database.db **SQLite database file**

## 🚀 Setup & Installation

## ⚙️ Prerequisits

- **Python 3.8+**
- **SQLite3** (comes preinstalled with Python)
- **pipenv** (optional, for managing dependencies)

1. **Clone this repository:**
   
   git clone https://github.com/yourusername/phase-3-project-GEORGE_MUKOSHI.git

2. Navigate to the project folder  
-  cd phase-3-project-GEORGE_MUKOSHI/

3. Run the project
- python3 main.py

## Usage

- ## 🧰 Usage

Follow these steps to use the **Asset Inventory Management CLI Application**:

1. **Activate the virtual environment**
   ```bash
   source venv/bin/activate     # (Mac/Linux)

2. python3 main.py

3.Below is an overview display 

🚀 Welcome to the Asset Management System...

 Main Menu
1. Manage Employees
2. Manage Assets
3. Generate Reports
4. Exit
Enter choice:

## Features

- Full CRUD functionality (Create, Read, Update, Delete)
- One-to-many relationships between employees and assets
- Asset summary report generation
- Data validation and clean error handling

## Technologies Used

- python3
- SQlite3
- os module
- venv

## License
- This project is licensed under the MIT License.

## Author
- George Imbiakha Mukoshi
