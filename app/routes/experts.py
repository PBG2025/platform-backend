# app/routes/experts.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_experts():
    return [{"id": 1, "specialty": "Reservoir"}]

