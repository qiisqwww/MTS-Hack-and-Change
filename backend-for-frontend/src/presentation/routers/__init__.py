from fastapi import APIRouter

from .healthcheck import healthcheck_router
from .get_info import get_info_router
from .filter_employees import filter_employees_router
from .find_boss import find_boss_router
from .find_subs import find_subs_router

__all__ = [
    "root_router"
]


root_router = APIRouter(prefix="/api")
root_router.include_router(healthcheck_router)
root_router.include_router(get_info_router)
root_router.include_router(filter_employees_router)
root_router.include_router(find_boss_router)
root_router.include_router(find_subs_router)
