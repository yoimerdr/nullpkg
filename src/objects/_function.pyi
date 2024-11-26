from typing import Sequence, Union
from ..utils import NameIndentable, ReturnType, Nameable
from ..variables import Parameter

_Params: Union = Sequence[str] | Sequence[Parameter]
_Parameter: Union = Parameter | str
_Type: Union = ReturnType | str


class Function(NameIndentable):
    def __init__(self, name: str | Nameable, params: _Params = None, level: int = 0, return_value=None,
                 return_type: _Type = None, ): ...

    @property
    def params(self) -> dict[str, Parameter]: ...

    @params.setter
    def params(self, params: _Params): ...

    def append(self, param: _Parameter): ...

    def remove(self, param: _Parameter): ...

    def clear(self): ...

    @property
    def returnType(self) -> _Type: ...

    @returnType.setter
    def returnType(self, return_type: _Type): ...

    @property
    def returnValue(self) -> str: ...

    @returnValue.setter
    def returnValue(self, value):
        def __str__(self): ...
