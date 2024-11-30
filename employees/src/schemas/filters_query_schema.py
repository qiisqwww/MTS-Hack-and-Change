from pydantic import BaseModel, EmailStr

__all__ = [
    "FiltersQuerySchema"
]


class FiltersQuerySchema(BaseModel):
    department_id: int
    post_id: int
    role_id: int
    first_name: str
    last_name: str
    phone_number: str
    city: str
    address: str
    email: EmailStr
    tg_username: str
