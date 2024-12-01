from datetime import date

from pydantic import BaseModel, EmailStr

from src.enums import SexEnum
from src.schemas.on_leave_schema import OnLeaveSchema
from src.schemas.on_sick_leave_schema import OnSickLeaveSchema

__all__ = [
    "EmployeeReturnSchema",
]


class EmployeeReturnSchema(BaseModel):
    id: int
    post: str | None
    department_path: str | None
    department_name: str | None
    first_name: str | None
    last_name: str | None
    birthdate: date | None
    sex: str | None
    phone_number: str | None
    city: str | None
    address: str | None
    tg_username: str | None
    email: EmailStr | None
    on_sick_leave_info: OnSickLeaveSchema | None
    on_leave_info: OnLeaveSchema | None
    boss_id: int | None
    about: str | None
