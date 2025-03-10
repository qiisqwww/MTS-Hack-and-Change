from fastapi import APIRouter, Depends

from src.services import EmployeesService
from src.get_service import get_employees_service
from src.schemas import FiltersSchema


get_filtered_employees_router = APIRouter()


@get_filtered_employees_router.post("/filter")
async def get_filtered_employees(
        filters: FiltersSchema,
        employees_service: EmployeesService = Depends(get_employees_service)
) -> dict:
    filtered_employees = await employees_service.filter_employees_by_parameters(filters)

    return {"filtered_employees": filtered_employees}
