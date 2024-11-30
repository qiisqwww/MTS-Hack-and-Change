from fastapi import APIRouter, Depends

from src.get_service import get_departament_service
from src.services import DepartmentService

__all__ = [
    "get_all_router"
]


get_all_router = APIRouter()


@get_all_router.get("/all")
async def get_all(department_service: DepartmentService = Depends(get_departament_service)):
    return await department_service.get_all_departments()
