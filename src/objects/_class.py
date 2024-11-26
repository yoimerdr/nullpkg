from ._class_method import ClassMethod
from ..variables import Variable
from ..utils import NameIndentable, getName, Type, to

__all__ = ('Class',)


class Class(NameIndentable):
    def __init__(self, name, methods=None, superclass=None, level=0, ):
        super(Class, self).__init__(name, level)
        self.__methods = None
        self.methods = methods
        self.superclass = superclass

    @property
    def methods(self):
        return self.__methods

    @methods.setter
    def methods(self, value):
        if self.__methods is None:
            self.__methods = {}
        else:
            self.__methods.clear()
        if value:
            for item in value:
                self.append(item)

    def append(self, method):
        if not isinstance(method, (Class, Variable)):
            method = to(method, ClassMethod)
        method = self.__changeLevel(method)
        self.__methods[getName(method)] = method

    def remove(self, method):
        self.__methods.pop(getName(method))

    def clear(self):
        self.__methods.clear()

    @property
    def superclass(self):
        return self.__superclass

    @superclass.setter
    def superclass(self, value):
        self.__superclass = None if not value else to(value, Type)

    def __changeLevel(self, method):
        method.level = self.level + 1
        return method

    def copy(self):
        cls = Class(
            self.name,
            [],
            self.superclass,
            self.level,
        )
        cls.__methods = self.methods

    def __str__(self):
        return "{}class {}{}: {}\n".format(
            self.indent,
            self.name,
            '' if not self.superclass else '({})'.format(self.superclass),
            ' pass' if not self.methods else ''.join(
                map(str, map(self.__changeLevel, self.methods.values()))
            )
        )
