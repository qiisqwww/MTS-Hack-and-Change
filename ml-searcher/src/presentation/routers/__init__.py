from fastapi import APIRouter

from .healthcheck import healthcheck_router

__all__ = [
    "root_router"
]


root_router = APIRouter()
root_router.include_router(healthcheck_router)
