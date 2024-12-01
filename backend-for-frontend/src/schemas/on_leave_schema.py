from datetime import date

from pydantic import BaseModel

__all__ = [
    "OnLeaveSchema",
]


class OnLeaveSchema(BaseModel):
    date_from: str
    date_to: str
