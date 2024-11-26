import collections

from ._import import Import
from ..utils import PathNode, getName, paths, getFullname

__all__ = ('File',)


class File(PathNode):
    def __init__(self, name, items=None, imports=None, ):
        super(File, self).__init__(name)
        self.__items = None
        self.__imports = None
        self.items = items
        self.imports = imports

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = collections.OrderedDict(**{it.name: it for it in value} if value else {})

    @property
    def imports(self):
        return self.__imports

    @imports.setter
    def imports(self, value):
        if self.__imports is None:
            self.__imports = {}
        else:
            self.__imports.clear()
        if value:
            for it in value:
                self._appendImport(it)

    def _appendImport(self, value):
        self.__imports[value.fullname] = value

    def append(self, item):
        name = item.name
        target = self.__items
        if isinstance(item, Import):
            name = item.fullname
            target = self.__imports
        target[name] = item

    def remove(self, name):
        self.__items.pop(getName(name))

    def removeImport(self, name):
        self.__imports.pop(getFullname(name))

    def clear(self):
        self.__items.clear()
        self.__imports.clear()

    def _create(self):
        with open("{}.py".format(self.fullname), "wb") as fs:
            fs.write(str(self).encode("utf-8"))

    def create(self):
        if self.parent:
            paths.mkdir(self.parent, parents=True, exist_ok=True)
            for parent in self.parents:
                with open("{}/__init__.py".format(parent.fullname), "wb+") as _:
                    pass
        self._create()

    def __str__(self):
        imports = ''.join(map(str, self.imports.values()))
        if imports:
            imports += "\n\n"
        return "{}{}\n".format(
            imports,
            ''.join(map(str, self.items.values())),
        )
