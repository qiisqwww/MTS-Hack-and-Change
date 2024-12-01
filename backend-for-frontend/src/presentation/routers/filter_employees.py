from typing import List

from fastapi import APIRouter, Query, Depends
from pydantic import EmailStr

from src.get_service import get_sub_services_manager_service
from src.services import SubServicesManagerService
from src.schemas import FiltersSchema, EmployeeReturnSchema

__all__ = [
    "filter_employees_router",
]


filter_employees_router = APIRouter()


@filter_employees_router.get("/filter", response_model=List[EmployeeReturnSchema])
async def filter_employees(
        sub_services_manager_service: SubServicesManagerService = Depends(get_sub_services_manager_service),
        department_name: str | None = Query(None),
        post: str | None = Query(None),
        role: str | None = Query(None),
        first_name: str | None = Query(None),
        last_name: str | None = Query(None),
        phone_number: str | None = Query(None),
        city: str | None = Query(None),
        address: str | None = Query(None),
        email: EmailStr | None = Query(None),
        tg_username: str | None = Query(None),
        prompt: str | None = Query(None)
):
    filters = FiltersSchema(
        department_name=department_name,
        post=post,
        role=role,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        city=city,
        address=address,
        email=email,
        tg_username=tg_username
    )

    return await sub_services_manager_service.filter_employees(filters, prompt)
