from fastapi import APIRouter, Depends, Query

from src.services import EmployeesService
from src.get_service import get_employees_info_service
from src.schemas import FilterSchema, EmployeeReturnSchema


get_filtered_employees_router = APIRouter()


@get_filtered_employees_router.get("/filter", response_model=EmployeeReturnSchema)
async def get_filtered_employees(
        employees_info_service: EmployeesService = Depends(get_employees_info_service),
        filters: FilterSchema = Query(),
):