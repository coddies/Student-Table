from sqlalchemy import Column, Integer, String
from database import Base

# Each instance of this class = one row in the 'students' table
class Student(Base):
    __tablename__ = "students"

    id         = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name  = Column(String)
    email      = Column(String, unique=True, index=True)
    password   = Column(String)  # Hash this in production!
