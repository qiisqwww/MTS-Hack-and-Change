from fastapi import APIRouter, Depends, Query, HTTPException, status

from src.services import EmployeesService
from src.get_service import get_employees_service


find_employee_router = APIRouter()


@find_employee_router.get("/employee")
async def find_employee(
        employee_id: int = Query(),
        employees_service: EmployeesService = Depends(get_employees_service)
):
    found_employee = await employees_service.find_employee_by_id(employee_id)

    if not found_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="employee was not found"
        )

    return found_employee
