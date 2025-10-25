from pydantic import BaseModel, validator
from typing import Optional

# -----------------------
# User Schemas
# -----------------------
class UserCreate(BaseModel):
    username: str
    password: str
    role: str

    @validator("password")
    def numeric_password(cls, v):
        if not v.isdigit():
            raise ValueError("Password must contain only numbers")
        if len(v) > 72:
            v = v[:72]  # truncate to safe length
        return v

class UserOut(BaseModel):
    id: int
    username: str
    role: str
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

# -----------------------
# Startup Schemas
# -----------------------
class StartupCreate(BaseModel):
    name: str
    founder: str

class StartupOut(StartupCreate):
    id: int
    class Config:
        orm_mode = True

# -----------------------
# Grant Schemas
# -----------------------
class GrantCreate(BaseModel):
    startup_name: str
    amount: float

class GrantOut(GrantCreate):
    id: int
    status: str
    class Config:
        orm_mode = True

# -----------------------
# Facility Schemas
# -----------------------
class FacilityCreate(BaseModel):
    name: str
    type: str

class FacilityOut(FacilityCreate):
    id: int
    status: str
    class Config:
        orm_mode = True

# -----------------------
# Mentor Schemas
# -----------------------
class MentorCreate(BaseModel):
    name: str
    expertise: str

class MentorOut(MentorCreate):
    id: int
    class Config:
        orm_mode = True
