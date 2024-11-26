import builtins
from typing import Union, Sequence, Literal

from ._function import Function
from ..utils import ReturnType, Nameable
from ..variables import Parameter

class ClassMethodType:
    STATIC: Literal['static']
    CLASS: Literal['class']
    OWN: Literal['own']


_MethodType: Union = Literal['static', 'class', 'own']
_Params: Union = Sequence[str] | Sequence[Parameter]
_ReturnType: Union = ReturnType | str


class ClassMethod(Function):
    def __init__(self, name: str | Nameable, params: _Params = None, level: int = 1, return_value=None,
                 return_type: _ReturnType = None, type: _MethodType = ClassMethodType.OWN):
        ...

    @staticmethod
    def magic(name: str, params: _Params = None, level: int = 1, return_value=None, return_type: _ReturnType = None): ...

    @staticmethod
    def init(params: _Params = None, level: int = 1, ): ...

    @staticmethod
    def str(params: _Params = None, level: int = 1, ): ...

    @property
    def type(self) -> _MethodType:

    @type.setter
    def type(self, value: _MethodType): ...

    def copy(self) -> ClassMethod: ...

    def __str__(self) -> builtins.str: ...
