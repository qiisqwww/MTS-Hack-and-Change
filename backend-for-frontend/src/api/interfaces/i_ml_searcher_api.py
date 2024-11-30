from abc import ABC, abstractmethod

__all__ = [
    "IMLSearcherApi"
]


class IMLSearcherApi(ABC):
    @abstractmethod
    async def filter_by_prompt(self, prompt: str, employees: list) -> list[int]:
        ...
