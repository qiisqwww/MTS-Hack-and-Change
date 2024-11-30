from enum import StrEnum, verify, UNIQUE

__all__ = [
    "SexEnum"
]


@verify(UNIQUE)
class SexEnum(StrEnum):
    MAN = "М"
    WOMAN = "Ж"
