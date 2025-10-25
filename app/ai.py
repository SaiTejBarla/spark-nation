from fastapi import APIRouter
from pydantic import BaseModel
import random

router = APIRouter(tags=["AI Evaluation"])

class EvaluationRequest(BaseModel):
    startup_name: str
    pitch: str

class EvaluationResponse(BaseModel):
    score: float
    feedback: str

@router.post("/ai/evaluate", response_model=EvaluationResponse, summary="AI evaluates startup pitch")
async def evaluate_startup(data: EvaluationRequest):
    score = round(random.uniform(60, 95), 2)
    feedback = f"'{data.startup_name}' has strong potential. Improve {random.choice(['market focus', 'financial clarity', 'team expertise', 'scalability'])}."
    return {"score": score, "feedback": feedback}
