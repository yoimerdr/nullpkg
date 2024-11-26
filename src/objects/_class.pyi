from typing import Union, Sequence

from ._class_method import ClassMethod
from ..variables import Variable
from ..utils import NameIndentable, Nameable, Type

_AnyItem: Union = ClassMethod | str | Class | Variable
_AnyMethods: Union = Sequence[str] | Sequence[ClassMethod] | Sequence[Class]
_AnyNamebale: Union = Nameable | str
_AnyType: Union = Type | str

class Class(NameIndentable):
    def __init__(self, name: _AnyNamebale, methods: _AnyMethods = None, superclass: _AnyType = None, level: int = 0, ): ...

    @property
    def methods(self) -> dict[str, ClassMethod | Class | Variable]: ...

    @methods.setter
    def methods(self, value: _AnyMethods): ...

    def append(self, method: _AnyItem): ...

    def remove(self, method: _AnyItem): ...

    def clear(self): ...

    @property
    def superclass(self) -> Type: ...

    @superclass.setter
    def superclass(self, value: _AnyType): ...

    def copy(self) -> Class: ...

    def __str__(self) -> str: ...
