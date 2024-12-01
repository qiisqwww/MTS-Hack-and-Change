from fastapi import APIRouter, Depends

from src.get_service import get_sub_services_manager_service
from src.services import SubServicesManagerService


get_info_router = APIRouter()


@get_info_router.get("/info")
async def get_info(
        sub_services_manager_service: SubServicesManagerService = Depends(get_sub_services_manager_service)
) -> None:
    return await sub_services_manager_service.get_info()
