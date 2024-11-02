from fastapi import APIRouter
from app.routers.calculate import router as calculate_router
from app.routers.operations import router as operations_router


routers = APIRouter()
router_list = [
    calculate_router,
    operations_router,
]

for router in router_list:
    routers.include_router(router)
