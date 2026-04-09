from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from database import engine, Base, SessionLocal
import models

# Create all tables defined in models.py on startup
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow all origins so the frontend HTML file can call this API freely
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Pydantic Schemas ---

class StudentCreate(BaseModel):
    """Validates the request body for creating/updating a student."""
    first_name: str
    last_name: str
    email: str
    password: str

class StudentResponse(BaseModel):
    """What we return to the client — password is intentionally excluded."""
    id: int
    first_name: str
    last_name: str
    email: str

    class Config:
        from_attributes = True  # Allows Pydantic to read SQLAlchemy model attributes


# --- DB Dependency ---

def get_db():
    """Opens a session for the request, then closes it in the finally block."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- CRUD Endpoints ---

@app.get("/students/", response_model=list[StudentResponse])
def get_all_students(db: Session = Depends(get_db)):
    """Return every student record from the database."""
    return db.query(models.Student).all()


@app.post("/students/", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    """Create a new student; raise 400 if the email already exists."""
    if db.query(models.Student).filter(models.Student.email == student.email).first():
        raise HTTPException(status_code=400, detail="Email already registered.")

    new_student = models.Student(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)  # Reload from DB to get the auto-generated id
    return new_student


@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    """Find the student by id, update its fields, and commit the changes."""
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found.")

    for field, value in student.model_dump().items():
        setattr(db_student, field, value)

    db.commit()
    db.refresh(db_student)
    return db_student


@app.delete("/students/{student_id}", status_code=200)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    """Delete the student with the given id or raise 404 if not found."""
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found.")

    db.delete(db_student)
    db.commit()
    return {"message": f"Student {student_id} deleted successfully."}
