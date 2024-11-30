from pydantic import BaseModel

__all__ = [
    "FiltersSchema",
]


class FiltersSchema(BaseModel):
    department_name: str | None
    post: str | None
    role: str | None
    first_name: str | None
    last_name: str | None
    phone_number: str | None
    city: str | None
    address: str | None
    email: str | None
    tg_username: str | None
