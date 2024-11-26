from typing import Union, Sequence

from ._import import Import
from ..objects import Class, Function
from ..variables import Variable

from ..utils import Nameable, PathNode

_AnyNameable: Union = Nameable | str
_FileItems: Union = Sequence[Class] | Sequence[Function] | Sequence[Variable]
_FileItem: Union = Class | Function | Variable
_FileImports: Union = Sequence[Import]


class File(object, PathNode):
    def __init__(self, name: _AnyNameable, items: _FileItems = None, imports: _FileImports = None, ): ...
    @property
    def items(self) -> dict[str, _FileItem]: ...

    @items.setter
    def items(self, value: _FileItems): ...

    @property
    def imports(self) -> dict[str, Import]: ...

    @imports.setter
    def imports(self, value: _FileImports): ...

    def append(self, item: _FileItem | Import): ...

    def remove(self, name: _AnyNameable): ...

    def removeImport(self, name: _AnyNameable): ...

    def clear(self): ...

    def create(self): ...

    def __str__(self) -> str: ...
