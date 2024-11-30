from datetime import date

from pydantic import BaseModel, EmailStr, ConfigDict

from src.enums import SexEnum

__all__ = [
    "EmployeeSchema",
]


class EmployeeSchema(BaseModel):
    id: int
    post_id: int
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
    is_on_sick_leave: bool
    is_on_leave: bool
    boss_id: int

    model_config = ConfigDict(from_attributes=True)
