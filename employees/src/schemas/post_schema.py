from pydantic import BaseModel, ConfigDict

__all__ = [
    "PostSchema"
]


class PostSchema(BaseModel):
    id: int
    name: str
    role_id: int

    model_config = ConfigDict(from_attributes=True)
