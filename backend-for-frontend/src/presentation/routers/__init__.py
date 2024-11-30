from fastapi import APIRouter

from .healthcheck import healthcheck_router
from .get_info_router import get_info_router

__all__ = [
    "root_router"
]


root_router = APIRouter(prefix="/api")
root_router.include_router(healthcheck_router)
root_router.include_router(get_info_router)
