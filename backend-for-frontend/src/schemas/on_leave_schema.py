from datetime import date

from pydantic import BaseModel

__all__ = [
    "OnLeaveSchema",
]


class OnLeaveSchema(BaseModel):
    date_from: date
    date_to: date
