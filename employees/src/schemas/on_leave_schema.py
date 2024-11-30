from datetime import date

from pydantic import BaseModel, ConfigDict

__all__ = [
    "OnLeaveSchema",
]


class OnLeaveSchema(BaseModel):
    employee_id: int
    date_from: date
    date_to: date

    model_config = ConfigDict(from_attributes=True)
