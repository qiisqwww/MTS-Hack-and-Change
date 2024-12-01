from fastapi import APIRouter

from .healthcheck import healthcheck_router
from .get_all import get_all_router
from .get_filtered_employees import get_filtered_employees_router
from .find_employee import find_employee_router
from .find_subs import find_subs_router

__all__ = [
    "root_router"
]


root_router = APIRouter(prefix="/api")
root_router.include_router(healthcheck_router)
root_router.include_router(get_all_router)
root_router.include_router(get_filtered_employees_router)
root_router.include_router(find_employee_router)
root_router.include_router(find_subs_router)
