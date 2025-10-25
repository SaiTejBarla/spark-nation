from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)  # admin, startup, mentor

class Startup(Base):
    __tablename__ = "startups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    founder = Column(String)

class Grant(Base):
    __tablename__ = "grants"
    id = Column(Integer, primary_key=True, index=True)
    startup_name = Column(String)
    amount = Column(Float)
    status = Column(String, default="pending")

class Facility(Base):
    __tablename__ = "facilities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    type = Column(String)
    status = Column(String, default="available")

class Mentor(Base):
    __tablename__ = "mentors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    expertise = Column(String)
