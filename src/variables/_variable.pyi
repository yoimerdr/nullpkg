from typing import TypeVar, Generic, Union

from ..utils import NameTypeIndentable, Nameable, Typeable

_AnyNameable: Union = Nameable | str

_AnyTypeable: Union = Typeable | str

_T = TypeVar("_T")

class Variable(NameTypeIndentable, Generic[_T]):
    def __init__(self, name: _AnyNameable, value: _T = None, level: int = 0, type: _AnyTypeable = None): ...
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: _T): ...
    def __str__(self) -> str: ...
