from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from .database import Base, get_db

router = APIRouter()

class Facility(Base):
    __tablename__ = "facilities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    type = Column(String)
    status = Column(String, default="available")

@router.post("/facilities/")
def create_facility(name: str, type: str, db: Session = Depends(get_db)):
    existing = db.query(Facility).filter(Facility.name == name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Facility already exists")
    facility = Facility(name=name, type=type)
    db.add(facility)
    db.commit()
    db.refresh(facility)
    return facility

@router.get("/facilities/")
def list_facilities(db: Session = Depends(get_db)):
    return db.query(Facility).all()
