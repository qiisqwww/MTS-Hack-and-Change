from datetime import date

from pydantic import BaseModel, EmailStr

from src.enums import SexEnum
from src.schemas.on_leave_schema import OnLeaveSchema
from src.schemas.on_sick_leave_schema import OnSickLeaveSchema


class EmployeeReturnSchema(BaseModel):
    post_id: int
    functional_block_id: int
    department_id: int
    first_name: str
    middle_name: str
    last_name: str
    birth_date: date
    sex: SexEnum
    phone_number: str
    city: str
    address: str
    tg_username: str
    email: EmailStr
    on_sick_leave_info: OnSickLeaveSchema | None
    on_leave_info: OnLeaveSchema | None
    boss_id: int
