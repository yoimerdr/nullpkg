from ._indentable import Indentable
from ._typeable import Typeable
from ._nameable import Nameable

__all__ = ('NameTypeable', 'NameIndentable', 'NameTypeIndentable')


class NameIndentable(Nameable, Indentable):
    def __init__(self, name, level):
        Nameable.__init__(self, name)
        Indentable.__init__(self, level)


class NameTypeIndentable(NameIndentable, Typeable):
    def __init__(self, name, level, type):
        NameIndentable.__init__(self, name, level)
        Typeable.__init__(self, type)


class NameTypeable(Nameable, Typeable):
    def __init__(self, name, type):
        Nameable.__init__(self, name)
        Typeable.__init__(self, type)
