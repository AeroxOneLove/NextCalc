from fastapi import APIRouter

from app.schemas.operation_schema import OperationSchema
from app.services.operation_service import OperationService


router = APIRouter()


@router.get("/operations", response_model=OperationSchema)
async def operations():
    return OperationService().get_all_operations()
