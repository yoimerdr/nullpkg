import builtins
from typing import Any


class Value:
    def __init__(self, value: Any): ...

    @property
    def value(self) -> Any: ...

    @value.setter
    def value(self, value): ...

    @staticmethod
    def callable(value) -> Value: ...

    @staticmethod
    def str(value, char='"') -> Value: ...

    def __str__(self) -> builtins.str: ...
