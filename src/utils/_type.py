from ._nodes import ImportPathNode
from ._fn import to
from ._nameable import Nameable, getName

__all__ = ('Type', 'VarType', 'ReturnType')


class Type(Nameable):

    def __init__(self, name):
        if isinstance(name, Type):
            self.module = name._module
            self._name = name._name
            return
        self._module = None
        super(Type, self).__init__(name)

    def _validatename(self, name):
        if '.' in name and name != '...':
            modules = name.split('.')
            self.module = modules[:-1]
            name = modules[-1]

        return super(Type, self)._validatename(name)

    @property
    def module(self):
        return self._module

    @module.setter
    def module(self, module):
        self._module = to(module, ImportPathNode)

    @property
    def fullname(self):
        if not self.module:
            return self.name
        return "{}.{}".format(self.module, self.name)

    @staticmethod
    def generic(name, *types):
        name = to(name, Nameable)
        if types:
            name = "{}[{}]".format(name, ', '.join(map(getName, map(lambda x: to(x, Type), types))))
        return Type(name)

    @staticmethod
    def iterable(name, type):
        return Type.generic(name, type, "...")

    @staticmethod
    def of(value, short=False):
        tp = type(value) if not isinstance(value, type) else value
        if short:
            return tp.__name__
        tp = str(tp)

        c = "'"
        st = tp.find(c)
        if st < 0:
            c = '"'
            st = tp.find(c)

        st += 1
        ed = tp.find(c, st)
        return Type(tp[st:ed])

    def __str__(self):
        return self.fullname


class VarType(Type):
    def __str__(self):
        return ": {}".format(self.fullname)


class ReturnType(Type):

    def __str__(self):
        return "-> {}".format(self.fullname)
