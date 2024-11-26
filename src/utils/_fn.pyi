from typing import TypeVar, Any

_T = TypeVar("_T")


def to(value: Any, cls: type[_T], copy: bool = False, **kwargs) -> _T: ...
def printable(value: _T) -> _T | str: ...