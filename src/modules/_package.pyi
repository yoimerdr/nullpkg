from typing import Union, Sequence

from ._file import File
from ._import import Import
from ..objects import Class, Function
from ..variables import Variable

from ..utils import Nameable

_AnyNameable: Union = Nameable | str
_FileItems: Union = Sequence[Class] | Sequence[Function] | Sequence[Variable] | Sequence[File]
_FileItem: Union = Class | Function | Variable | File
_FileImports: Union = Sequence[Import]


class Package(File):
    def __init__(self, name: _AnyNameable, packages: Sequence[File] = None, items: _FileItems = None,
                 imports: _FileImports = None, ): ...

    @property
    def packages(self) -> dict[str, File]: ...

    @packages.setter
    def packages(self, value: Sequence[File]): ...

    def append(self, item: _FileItem | Import): ...

    def removePackage(self, name: _AnyNameable): ...
