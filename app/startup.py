from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from .database import Base, get_db

router = APIRouter()

class Startup(Base):
    __tablename__ = "startups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    founder = Column(String)

@router.post("/startups/")
def create_startup(name: str, founder: str, db: Session = Depends(get_db)):
    existing = db.query(Startup).filter(Startup.name == name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Startup already exists")
    startup = Startup(name=name, founder=founder)
    db.add(startup)
    db.commit()
    db.refresh(startup)
    return startup

@router.get("/startups/")
def list_startups(db: Session = Depends(get_db)):
    return db.query(Startup).all()
