from fastapi import APIRouter

from app.services.calculate_service import CalculateService


router = APIRouter()


@router.post("/caculate", response_model=float)
async def caculate(expression: str):
    return CalculateService().calculate(expression)
