from fastapi import APIRouter, Depends
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from .database import Base, get_db

router = APIRouter()

class Mentor(Base):
    __tablename__ = "mentors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    expertise = Column(String)

@router.post("/mentors/")
def create_mentor(name: str, expertise: str, db: Session = Depends(get_db)):
    mentor = Mentor(name=name, expertise=expertise)
    db.add(mentor)
    db.commit()
    db.refresh(mentor)
    return mentor

@router.get("/mentors/")
def list_mentors(db: Session = Depends(get_db)):
    return db.query(Mentor).all()
