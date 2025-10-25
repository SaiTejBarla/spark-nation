from fastapi import APIRouter

router = APIRouter(tags=["Analytics Dashboard"])

@router.get("/analytics/overview", summary="View dashboard analytics")
def get_analytics():
    return {
        "total_startups": 42,
        "active_grants": 7,
        "total_mentors": 12,
        "avg_ai_score": 84.3,
        "top_domain": "AI & Sustainability"
    }
