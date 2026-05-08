# 🎓 Department Information Management System
### COMP6003 – Software Design and Development | S1, 2026
### University of Notre Dame Australia — Fremantle & Sydney Campus

---

## 📌 Project Overview

The **Department Information Management System (DIMS)** is a web-based application built for the **Department of Computer Science** at the University of Notre Dame Australia. It provides a centralized platform for students, faculty, and administrators to access and manage academic information including programs, courses, student records, classrooms, and semester schedules.

The system is built using **Python Flask** as the backend framework and **SQLite** as the database, following **Object-Oriented Programming (OOP)** principles to ensure modularity, maintainability, and scalability.

---

## 👥 Group Information

| Field            | Details                              |
|------------------|--------------------------------------|
| **Group Name**   | Group [X]                            |
| **Project Title**| Department Information Management System |
| **Course**       | COMP6003 – Software Design and Development |
| **Semester**     | Semester 1, 2026                     |
| **Campus**       | Sydney                               |

### Group Members

| Name             | Student ID  | Role               |
|------------------|-------------|--------------------|
| [Member 1 Name]  | [ID]        | Project Leader     |
| [Member 2 Name]  | [ID]        | Developer          |
| [Member 3 Name]  | [ID]        | Developer          |
| [Member 4 Name]  | [ID]        | Developer          |

> **Project Leader:** [Name] — responsible for managing the main branch, reviewing and approving Pull Requests, and ensuring repository integrity.

---

## 🛠️ Tech Stack

| Layer        | Technology              |
|--------------|-------------------------|
| Backend      | Python 3.x, Flask       |
| Database     | SQLite3, SQLite Studio  |
| Frontend     | HTML5, CSS3, Jinja2     |
| Version Control | Git, GitHub          |
| IDE          | PyCharm / VS Code       |
| Testing      | Python `unittest`       |
| Methodology  | Agile (Scrum Sprints)   |

---

## 📁 Project Structure

```
DIMS/
├── app.py                  # Main Flask application entry point
├── database.db             # SQLite database file
├── schema.sql              # SQL schema for database setup
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── models/                 # OOP class definitions
│   ├── __init__.py
│   ├── program.py          # Program class
│   ├── course.py           # Course class
│   ├── student.py          # Student class
│   └── classroom.py        # Classroom class
│
├── routes/                 # Flask route blueprints
│   ├── __init__.py
│   ├── programs.py
│   ├── courses.py
│   ├── students.py
│   └── classrooms.py
│
├── templates/              # Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   ├── programs.html
│   ├── courses.html
│   ├── students.html
│   └── classrooms.html
│
├── static/                 # CSS, JS, images
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── tests/                  # Unit test scripts
│   ├── test_program.py
│   ├── test_course.py
│   ├── test_student.py
│   └── test_classroom.py
│
└── evidence/               # Screenshots for submission
    ├── github_commits/
    ├── pull_requests/
    ├── database_tables/
    └── flask_ui/
```

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1 — Clone the Repository

```bash
git clone https://github.com/[group-name]/DIMS-COMP6003.git
cd DIMS-COMP6003
```

### Step 2 — Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Set Up the Database

```bash
python setup_db.py
```

This will create the `database.db` SQLite file and populate it with sample data.

### Step 5 — Run the Application

```bash
python app.py
```

Open your browser and navigate to: **http://127.0.0.1:5000**

---

## 🌐 Application Features

| Feature                  | Route                        | Description                                      |
|--------------------------|------------------------------|--------------------------------------------------|
| Home / Dashboard         | `/`                          | Overview of the department system               |
| Program Information      | `/programs`                  | View all programs with duration, credits, etc.  |
| Course Search            | `/courses`                   | Search courses by Program ID and Semester       |
| Student Search           | `/students`                  | Search student details by Student ID            |
| Classroom Information    | `/classrooms`                | View all classroom listings by campus           |

---

## 🗄️ Database Schema Summary

The application uses the following SQLite tables:

- **Programs** — stores program-level information (ID, name, duration, credits, course count)
- **Courses** — stores course details linked to programs and classrooms
- **Students** — stores student profiles including marks and attendance
- **Enrollments** — junction table linking students to their enrolled courses
- **Classrooms** — stores room details per building and campus

> See `schema.sql` for the full database schema with all constraints and relationships.

---

## 🧪 Running Unit Tests

```bash
# Run all tests
python -m unittest discover tests/

# Run a specific test file
python -m unittest tests/test_student.py
```

Each Python module includes a minimum of **2 unit test cases** verifying core functionality.

---

## 🔁 Agile Development — Sprint Summary

| Sprint | Duration         | Focus                                          |
|--------|------------------|------------------------------------------------|
| 1      | Week 1           | Project setup, database schema, OOP models    |
| 2      | Week 2           | Flask routes, program & course features       |
| 3      | Week 3           | Student search, classroom module, UI design   |
| 4      | Week 4           | Unit testing, debugging, integration          |
| Final  | Week 5           | Documentation, presentation prep, submission  |

---

## 🤖 AI Usage Declaration

| Field             | Details                                                 |
|-------------------|---------------------------------------------------------|
| AI Tool Used      | [e.g., Claude (Anthropic) / GitHub Copilot / ChatGPT]  |
| Purpose           | [e.g., Code suggestions, debugging assistance, documentation drafting] |

**How AI was used:** AI tools were used to assist with [specific usage, e.g., generating boilerplate code for Flask routes, suggesting SQL query structures]. All AI-generated suggestions were **reviewed, tested, and modified** by group members to ensure correctness, alignment with project requirements, and adherence to academic integrity guidelines. No AI-generated code was submitted without human review and understanding.

---

## 📜 License

This project was developed for academic purposes as part of COMP6003 at the University of Notre Dame Australia. All rights reserved by the respective group members.
