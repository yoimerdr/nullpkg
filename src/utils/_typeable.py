from ._type import VarType
from ._fn import to

__all__ = ('Typeable',)


class Typeable:
    def __init__(self, type=None):
        self.type = type

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if value is None:
            self._type = None
            return
        self._type = value.type if isinstance(value, Typeable) else to(value, VarType)
