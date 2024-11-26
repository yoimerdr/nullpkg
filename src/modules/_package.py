import collections

from ._file import File
from ._import import Import
from ..utils import getFullname, paths

__all__ = ('Package',)


class Package(File):
    def __init__(self, name, packages=None, items=None, imports=None):
        super(Package, self).__init__(name, items, imports)
        self.__packages = None
        self.packages = packages

    @property
    def packages(self):
        return self.__packages

    @packages.setter
    def packages(self, packages):
        if self.__packages is None:
            self.__packages = collections.OrderedDict()
        else:
            self.__packages.clear()
        if packages:
            for item in packages:
                self._appendPackage(item)

    def _appendImport(self, value):
        if not value.relative:
            value.relative = 1
        super(Package, self)._appendImport(value)

    def _appendPackage(self, package):
        parents = tuple(package.parents)
        target = parents[-1] if parents else package
        target._parent = self
        self.__packages[package.fullname] = package

    def append(self, item):
        if isinstance(item, File):
            self.__appendPackage(item)
            return
        super(Package, self).append(item)

    def removePackage(self, name):
        self.__packages.pop(getFullname(name))

    def clear(self):
        self.__packages.clear()
        super(Package, self).clear()

    def _create(self):
        paths.mkdir(self.fullname, parents=True, exist_ok=True)
        for file in self.packages.values():
            file.create()

        with open("{}/__init__.py".format(self.fullname), "wb") as fs:
            fs.write(str(self).encode("utf-8"))

    def __str__(self):
        pkg_import = None
        if self.imports:
            pkg_import = Import(".")
            for package in self.packages.values():
                parents = tuple(package.parents)
                last = parents[-2] if len(parents) > 1 else package
                pkg_import.append(last.name)
        return "{}\n{}".format(
            pkg_import if pkg_import else "",
            super(Package, self).__str__()
        )
