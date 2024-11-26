from typing import Union

from ._nameable import Nameable
from ._indentable import Indentable
from ._typeable import Typeable
from ._type import VarType

_AnyNameable: Union = Nameable | str

_AnyType: Union = VarType | _AnyNameable


class NameIndentable(Nameable, Indentable):
    def __init__(self, name: _AnyNameable, level: int): ...

class NameTypeIndentable(NameIndentable, Typeable):
    def __init__(self, name: _AnyNameable, level: int, type: _AnyType): ...

class NameTypeable(Nameable, Typeable):
    def __init__(self, name: _AnyNameable, type: _AnyType): ...
