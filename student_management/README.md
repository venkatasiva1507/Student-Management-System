🎓 Student Management System

A Full-Stack Web Application Built with Django & MySQL

A web-based application designed to simplify student record management with essential CRUD operations, search functionality, and MySQL database integration.

---

📌 Project Overview

The Student Management System provides a simple and organized interface to manage student information. It allows users to add, view, update, delete, and search student records efficiently.

✨ Key Features

- ➕ Add new student records
- 📋 View student details
- ✏️ Update existing records
- 🗑️ Delete student records
- 🔍 Search students by name, email, or course
- 🗄️ Store and manage data using MySQL
- 🖥️ User-friendly web interface

🛠️ Tech Stack

Technology| Purpose
Python| Backend programming
Django| Web framework
MySQL| Relational database
HTML5| Web page structure
CSS3| Styling and layout
JavaScript| Frontend interactivity
Git & GitHub| Version control

📂 Project Structure

Student-Management-System/
├── student_management/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── students/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── manage.py
├── .gitignore
└── README.md

⚙️ Installation & Setup

Prerequisites

- Python installed
- MySQL Server installed and running
- Git installed

1. Clone the Repository

git clone https://github.com/venkatasiva1507/Student-Management-System.git

2. Navigate to the Project

cd Student-Management-System

3. Create a Virtual Environment

python -m venv venv

Activate it on Windows PowerShell:

.\venv\Scripts\Activate.ps1

4. Install Dependencies

pip install django mysqlclient python-dotenv

5. Configure the Database

1. Create a MySQL database named "student_db".
2. Create a local ".env" file in the directory containing "manage.py".
3. Add your local database credentials using the variable names expected by "settings.py".
4. Ensure ".env" is listed in ".gitignore".

Security: Never commit your database password, ".env" file, or other secrets to GitHub.

6. Apply Migrations

python manage.py migrate

If model changes have not yet been migrated, run:

python manage.py makemigrations
python manage.py migrate

7. Run the Application

python manage.py runserver

Open your browser:

http://127.0.0.1:8000/

🎯 Learning Outcomes

- Built a Django application with CRUD functionality.
- Integrated Django with a MySQL database.
- Implemented student search and record management.
- Practiced database migrations and environment configuration.
- Used Git and GitHub for version control.

🚀 Future Enhancements

- User authentication and authorization
- Pagination for student records
- Improved responsive design
- Deployment to a cloud hosting platform

👨‍💻 Author

B. Venkat Siva

---

⭐ If you find this project useful, feel free to explore the repository and share feedback.
