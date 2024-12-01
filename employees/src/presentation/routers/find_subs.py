from fastapi import APIRouter, Depends, Query, HTTPException, status

from src.services import EmployeesService
from src.get_service import get_employees_service


find_subs_router = APIRouter()


@find_subs_router.get("/subs")
async def find_subs(
        employee_id: int = Query(),
        employees_service: EmployeesService = Depends(get_employees_service)
):
    found_subs = await employees_service.find_subs_by_employee_id(employee_id)

    if found_subs is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="employee was not found"
        )

    return found_subs
