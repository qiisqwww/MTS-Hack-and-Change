from fastapi import APIRouter, Depends, Query, HTTPException, status

from src.get_service import get_sub_services_manager_service
from src.services import SubServicesManagerService
from src.schemas import EmployeeReturnSchema


find_boss_router = APIRouter()


@find_boss_router.get("/boss", response_model=EmployeeReturnSchema)
async def get_info(
        sub_services_manager_service: SubServicesManagerService = Depends(get_sub_services_manager_service),
        boss_id: int = Query()
) -> None:
    boss = await sub_services_manager_service.find_employee_boss(boss_id)
    if boss is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    return await sub_services_manager_service.find_employee_boss(boss_id)
