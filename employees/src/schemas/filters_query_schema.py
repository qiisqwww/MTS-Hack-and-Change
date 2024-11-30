from pydantic import BaseModel, EmailStr

__all__ = [
    "FiltersQuerySchema"
]


class FiltersQuerySchema(BaseModel):
    department_id: int | None
    post_id: int | None
    role_id: int | None
    first_name: str | None
    last_name: str | None
    phone_number: str | None
    city: str | None
    address: str | None
    email: EmailStr | None
    tg_username: str | None
