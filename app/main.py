from fastapi import FastAPI

from app.schemas.operation_schema import OperationSchema
from app.services.calculate_service import CalculateService
from app.services.operation_service import OperationService

app = FastAPI()


@app.post("/caculate", response_model=float)
async def caculate(expression: str):
    return CalculateService().calculate(expression)


@app.get("/operations", response_model=OperationSchema)
async def operations():
    return OperationService().get_all_operations()
