from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.services import DepartmentService
from src.database import get_async_session
from src.repositories.impls import DepartmentRepository

__all__ = [
    "get_departament_service",
]


async def get_departament_service(session: AsyncSession = Depends(get_async_session)) -> DepartmentService:
    return DepartmentService(
        DepartmentRepository(session)
    )
