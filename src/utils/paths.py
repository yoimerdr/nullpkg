import errno
import os

from ._nodes import PathNode
from ._fn import to

__all__ = ('mkdir',)


def _mkdir(path, mode, parents, exist_ok):
    try:
        os.mkdir(path.fullname, mode)
    except OSError as e:
        if e.errno == errno.ENOENT:
            if not parents or not path.parent:
                raise
            _mkdir(path.parent, mode, True, True)
            _mkdir(path, mode, False, exist_ok)
        elif e.errno != errno.EEXIST or not exist_ok:
            raise


def mkdir(path, mode=0o777, parents=False, exist_ok=False):
    _mkdir(to(path, PathNode), mode, parents, exist_ok)
