This repository provides a basic CRUD (Create, Read, Update, Delete) operations implementation using Django and PostgreSQL. Additionally, it includes functionalities for searching and sorting data.

Features:

Create: Add new records to the database.
Read: Retrieve and display existing records from the database.
Update: Modify and update existing records in the database.
Delete: Remove records from the database.
Search: Search functionality to filter records based on specific criteria.
Sort: Sorting functionality to arrange records by name or time in ascending or descending order.


Requirements:
Python 
Django
PostgreSQL
psycopg2 (Python PostgreSQL adapter)

Installation:
Clone this repository.
Install Python (if not already installed).
Install Django using pip:
Copy code
pip install django
Install psycopg2:
Copy code
pip install psycopg2
Configure PostgreSQL database settings in settings.py.

Usage:
Run migrations to create necessary database tables:
Copy code
python manage.py migrate
Start the Django development server:
Copy code
python manage.py runserver

Access the application in your web browser at http://localhost:8000.
Access the application in your web browser at http://localhost:8000.
