from fastapi import APIRouter, Depends

from src.get_service import get_organization_service
from src.services import OrganizationService

__all__ = [
    "get_all_router"
]


get_all_router = APIRouter()


@get_all_router.get("/all")
async def get_all(department_service: OrganizationService = Depends(get_organization_service)):
    return await department_service.get_all()
