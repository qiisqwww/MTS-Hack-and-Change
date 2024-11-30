from datetime import date

from pydantic import BaseModel, EmailStr

from src.schemas.on_leave_schema import OnLeaveSchema
from src.schemas.on_sick_leave_schema import OnSickLeaveSchema

__all__ = [
    "EmployeeReturnSchema"
]


class EmployeeReturnSchema(BaseModel):
    post: str | None
    department_path: str | None
    department_name: str | None
    first_name: str
    last_name: str
    birthdate: date | None
    sex: str | None
    phone_number: str
    city: str
    address: str
    tg_username: str | None
    email: EmailStr | None
    on_sick_leave_info: OnSickLeaveSchema | None
    on_leave_info: OnLeaveSchema | None
    boss_id: int | None
    about: str
