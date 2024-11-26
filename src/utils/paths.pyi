from typing import AnyStr
from ._nodes import PathNode


def mkdir(path: AnyStr | PathNode, mode: int = 0o777, parents: bool = False, exist_ok: bool = False): ...
