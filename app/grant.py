from fastapi import APIRouter, Depends
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Session
from .database import Base, get_db

router = APIRouter()

class Grant(Base):
    __tablename__ = "grants"
    id = Column(Integer, primary_key=True, index=True)
    startup_name = Column(String)
    amount = Column(Float)
    status = Column(String, default="pending")

@router.post("/grants/")
def create_grant(startup_name: str, amount: float, db: Session = Depends(get_db)):
    grant = Grant(startup_name=startup_name, amount=amount)
    db.add(grant)
    db.commit()
    db.refresh(grant)
    return grant

@router.get("/grants/")
def list_grants(db: Session = Depends(get_db)):
    return db.query(Grant).all()
