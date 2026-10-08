# Todo REST API

A simple RESTful Todo API built with **Django** and **DRF**

This project provides user authentication and task management with support for searching, filtering, and ordering tasks.

This project currently focuses on the backend and REST API, with a frontend planned for a future version.

---
## Features 
- User registration 
- User login with Token Authentication
- Create, read, update, and delete tasks
- Search tasks by title and description
- Filter tasks by completion status
- Order tasks by creation date or due date
---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/MohammadMahdiGholinia/TodoProject.git
```

### 2. Create a virtual environment

```bash
python -m venv venv
```
Activate the virtual environment.

**Windows PowerShell:**

```bash
.\venv\Scripts\Activate.ps1
```

**Windows CMD:**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

`http://127.0.0.1:8000/`

---

# API Endpoints

## Authentication

**Register**

`POST /auth/register/`

**Login**

`POST /auth/login/`

## Tasks
All task endpoints require authentication.

**Get all tasks**

`GET /tasks/`

**Create a task**

`POST /tasks/`

**Get a single task**

`GET /task/<id>/`

**Update a task**

`PUT /task/<id>/`

`PATCH /task/<id>/`

PATCH can be used when only part of a task needs to be updated.

**Delete a task**

`DELETE /task/<id>/`

**Search**

`GET /task-list/?search=<query>`

The search is performed on:
- title
- description

**Filtering**

Tasks can be filtered by their completion status.

`GET /task-filter/?completed=true`

`GET /task-filter/?completed=false`

**Ordering**

Tasks can be ordered by creation date or due date.

`GET /task-ordering/?ordering=created_at`

`GET /task-ordering/?ordering=-created_at`

`GET /task-ordering/?ordering=due_date`

`GET /task-ordering/?ordering=-due_date`

---

## Development

This project is currently intended for learning and development purposes.
