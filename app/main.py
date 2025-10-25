from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
import shutil, random

from app.database import Base, engine, get_db
from app.models import User, Startup, Grant, Facility, Mentor
from app.schemas import *
from app.security import hash_password, verify_password, create_access_token, verify_token

# -----------------------
# Database setup
# -----------------------
Base.metadata.create_all(bind=engine)

# -----------------------
# FastAPI app
# -----------------------
app = FastAPI(title="Startup Incubator Platform")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# Root
# -----------------------
@app.get("/")
def read_root():
    return {"message": "Startup Incubator API is running"}

# -----------------------
# User Endpoints
# -----------------------
@app.post("/register/", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    user_obj = User(
        username=user.username,
        password_hash=hash_password(user.password),
        role=user.role.lower()
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj

@app.post("/login/", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": db_user.username, "role": db_user.role})
    return {"access_token": token, "token_type": "bearer"}

# -----------------------
# Role Protection
# -----------------------
def admin_required(current_user=Depends(verify_token)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin privileges required")
    return current_user

# -----------------------
# Startup CRUD
# -----------------------
@app.post("/startups/", response_model=StartupOut)
def create_startup(startup: StartupCreate, db: Session = Depends(get_db), user=Depends(admin_required)):
    existing = db.query(Startup).filter(Startup.name == startup.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Startup already exists")
    startup_obj = Startup(name=startup.name, founder=startup.founder)
    db.add(startup_obj)
    db.commit()
    db.refresh(startup_obj)
    return startup_obj

@app.get("/startups/", response_model=list[StartupOut])
def list_startups(db: Session = Depends(get_db), user=Depends(verify_token)):
    return db.query(Startup).all()

# -----------------------
# Grant CRUD
# -----------------------
@app.post("/grants/", response_model=GrantOut)
def create_grant(grant: GrantCreate, db: Session = Depends(get_db), user=Depends(admin_required)):
    grant_obj = Grant(startup_name=grant.startup_name, amount=grant.amount)
    db.add(grant_obj)
    db.commit()
    db.refresh(grant_obj)
    return grant_obj

@app.get("/grants/", response_model=list[GrantOut])
def list_grants(db: Session = Depends(get_db), user=Depends(verify_token)):
    return db.query(Grant).all()

# -----------------------
# Facility CRUD
# -----------------------
@app.post("/facilities/", response_model=FacilityOut)
def create_facility(facility: FacilityCreate, db: Session = Depends(get_db), user=Depends(admin_required)):
    existing = db.query(Facility).filter(Facility.name == facility.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Facility already exists")
    facility_obj = Facility(name=facility.name, type=facility.type)
    db.add(facility_obj)
    db.commit()
    db.refresh(facility_obj)
    return facility_obj

@app.get("/facilities/", response_model=list[FacilityOut])
def list_facilities(db: Session = Depends(get_db), user=Depends(verify_token)):
    return db.query(Facility).all()

# -----------------------
# Mentor CRUD
# -----------------------
@app.post("/mentors/", response_model=MentorOut)
def create_mentor(mentor: MentorCreate, db: Session = Depends(get_db), user=Depends(admin_required)):
    mentor_obj = Mentor(name=mentor.name, expertise=mentor.expertise)
    db.add(mentor_obj)
    db.commit()
    db.refresh(mentor_obj)
    return mentor_obj

@app.get("/mentors/", response_model=list[MentorOut])
def list_mentors(db: Session = Depends(get_db), user=Depends(verify_token)):
    return db.query(Mentor).all()

# -----------------------
# AI / Evaluation Module
# -----------------------
class EvaluationRequest(BaseModel):
    startup_name: str
    pitch: str

class EvaluationResponse(BaseModel):
    score: float
    feedback: str

@app.post("/ai/evaluate", response_model=EvaluationResponse)
def ai_evaluate(data: EvaluationRequest):
    score = round(random.uniform(60, 95), 2)
    feedback = f"'{data.startup_name}' has strong potential. Improve {random.choice(['market focus', 'financial clarity', 'team expertise', 'scalability'])}."
    return {"score": score, "feedback": feedback}

# -----------------------
# Analytics Dashboard (Mock)
# -----------------------
@app.get("/analytics/overview")
def analytics_overview():
    return {
        "total_startups": 42,
        "active_grants": 7,
        "total_mentors": 12,
        "avg_ai_score": 84.3,
        "top_domain": "AI & Sustainability"
    }

# -----------------------
# File / Video Uploads
# -----------------------
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/uploads/file")
def upload_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "status": "Uploaded successfully"}

# -----------------------
# Notifications / Communication (Mock)
# -----------------------
class Notification(BaseModel):
    recipient: str
    message: str

@app.post("/notify/send")
def send_notification(note: Notification):
    return {"sent_to": note.recipient, "message": note.message, "status": "Delivered (mock)"}

# -----------------------
# Role-Based Access (Mock)
# -----------------------
def get_current_user(role: str):
    if role.lower() not in ["admin", "startup", "mentor"]:
        raise HTTPException(status_code=403, detail="Invalid role")
    return {"username": "demo_user", "role": role.lower()}

@app.get("/role/{role}")
def role_access(role: str, user: dict = Depends(get_current_user)):
    return {"message": f"Access granted for {role} dashboard"}
