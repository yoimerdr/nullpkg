from typing import Union
from ._nameable import Nameable
from ._type import VarType

_AnyType: Union = VarType | str | Nameable


class Typeable:
    def __init__(self, type: _AnyType | Typeable = None): ...
    @property
    def type(self) -> VarType: ...
    @type.setter
    def type(self, type: _AnyType): ...
