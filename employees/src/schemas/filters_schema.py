from pydantic import BaseModel

__all__ = [
    "FilterSchema"
]


class FilterSchema(BaseModel):
    department_ids: list[int] | None
    functional_block_id: int | None
    post_id: int | None
    role: int | None
    first_name: str | None
    middle_name: str | None
    last_name: str | None
    phone_number: str | None
    city: str | None
    address: str | None
    email: str | None
