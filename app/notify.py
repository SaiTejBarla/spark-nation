from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["Notifications"])

class Notification(BaseModel):
    recipient: str
    message: str

@router.post("/notify/send", summary="Send notification (mock)")
def send_notification(note: Notification):
    return {"sent_to": note.recipient, "message": note.message, "status": "Delivered (mock)"}
