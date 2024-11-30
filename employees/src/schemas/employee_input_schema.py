from datetime import date

from pydantic import BaseModel, EmailStr

from src.enums import SexEnum

__all__ = [
    "EmployeeInputSchema",
]


class EmployeeInputSchema(BaseModel):
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
    boss_id: int
