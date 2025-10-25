from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

router = APIRouter(tags=["Role-Based Access"])

# Simulated user
def get_current_user(role: str = "Startup"):
    if role not in ["Admin", "Startup", "Mentor"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid role")
    return {"username": "demo_user", "role": role}

class AccessInfo(BaseModel):
    message: str

@router.get("/role/{role}", response_model=AccessInfo, summary="Access role-based data")
def get_role_dashboard(role: str, user=Depends(get_current_user)):
    return {"message": f"Access granted for {role} dashboard"}
