from fastapi import APIRouter, Depends, Query

from src.services import EmployeesService
from src.get_service import get_employees_service


find_employee_router = APIRouter()


@find_employee_router.get("/employee")
async def find_employee(
        employee_id: int = Query(),
        employees_service: EmployeesService = Depends(get_employees_service)
):
    return await employees_service.find_employee_by_id(employee_id)
