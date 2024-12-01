from typing import List

from fastapi import APIRouter, Depends, Query

from src.get_service import get_sub_services_manager_service
from src.services import SubServicesManagerService
from src.schemas import EmployeeReturnSchema


find_subs_router = APIRouter()


@find_subs_router.get("/subs", response_model=List[EmployeeReturnSchema])
async def get_subs(
        sub_services_manager_service: SubServicesManagerService = Depends(get_sub_services_manager_service),
        boss_id: int = Query()
) -> None:
    return await sub_services_manager_service.find_employee_subs(boss_id)
