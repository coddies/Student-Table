# Student Table — FastAPI + SQLAlchemy + Neon PostgreSQL

A full-stack CRUD application built with **FastAPI** (backend) and **Vanilla JS** (frontend).

## 📁 Project Structure

```
project/
├── backend/
│   ├── database.py   # SQLAlchemy engine & session setup
│   ├── models.py     # Student ORM model
│   └── main.py       # FastAPI app with CRUD endpoints
└── frontend/
    └── index.html    # Dark-themed dashboard UI
```

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Backend
```bash
cd backend
uvicorn main:app --reload
```

### 3. Open the Frontend
Open `frontend/index.html` in your browser.

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/students/` | Get all students |
| POST | `/students/` | Create a student |
| PUT | `/students/{id}` | Update a student |
| DELETE | `/students/{id}` | Delete a student |

## 🛠️ Tech Stack
- **Backend:** FastAPI, SQLAlchemy, Pydantic
- **Database:** Neon PostgreSQL
- **Frontend:** HTML, CSS, Vanilla JavaScript
