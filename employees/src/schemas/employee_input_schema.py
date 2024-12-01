from datetime import date

from pydantic import BaseModel, EmailStr

__all__ = [
    "EmployeeInputSchema",
]


class EmployeeInputSchema(BaseModel):
    post_id: int
    functional_block_id: int
    department_id: int
    first_name: str
    last_name: str
    birth_date: date
    sex: str
    phone_number: str
    city: str
    address: str
    tg_username: str
    email: EmailStr
    boss_id: int
