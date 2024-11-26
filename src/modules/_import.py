from ..utils import getName, ImportPathNode, Indentable, Nameable, to, getFullname

__all__ = ('Import', 'AliasImport')


class AliasImport(Nameable):
    def __init__(self, name, alias=None):
        Nameable.__init__(self, name)
        self.alias = alias

    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, alias):
        self.__alias = None if alias is None else to(alias, Nameable)

    def __str__(self):
        if not self.alias:
            return self.name
        return "{} as {}".format(self.name, self.alias)


class Import(ImportPathNode, Indentable):
    def __init__(self, name, imports=None, import_all=False, relative=0, level=0, alias=None):
        if name == ".":
            self._name = name
            self._parent = None
            if relative < 1:
                relative = 1
        else:
            ImportPathNode.__init__(self, name)
        Indentable.__init__(self, level)
        self.importAll = import_all
        self.relative = relative
        self.imports = imports
        self.alias = alias

    @staticmethod
    def of(value, imports=None, import_all=False, relative=0, level=0, alias=None):
        value = ImportPathNode.normalize(value)
        return Import(value, imports, import_all, relative, level, alias)

    @property
    def imports(self):
        return self.__imports

    @imports.setter
    def imports(self, imports):
        self.__imports = {getName(i): to(i, Nameable) for i in imports} if imports else {}

    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, alias):
        self.__alias = None if alias is None else to(alias, Nameable)

    @property
    def importAll(self):
        return self.__importAll

    @importAll.setter
    def importAll(self, import_all):
        self.__importAll = bool(import_all)

    @property
    def relative(self):
        return self.__relative

    @relative.setter
    def relative(self, relative):
        relative = 0 if not relative else relative
        if relative < 0:
            relative = 0
        elif relative > 2:
            relative = 2
        self.__relative = relative

    def append(self, name):
        self.__imports[getName(name)] = to(name, Nameable)

    def remove(self, name):
        self.__imports.pop(getName(name))

    def clear(self):
        self.__imports.clear()

    def __getImports(self):
        return '' if not self.__imports else ", ".join(map(str, self.imports.values()))

    def __str__(self):
        name = self.fullname if not self.relative else self.name
        if self.relative:
            rel_char = "." * self.relative
            if not self.importAll and not self.imports and self.parent:
                rel_char += self.parent.fullname
            else:
                name = self.fullname
            if self.importAll or self.imports:
                return "from {}{} import {}".format(
                    rel_char,
                    name if name != '.' else '',
                    '*' if self.importAll else self.__getImports()
                )
            elif name != '.':
                return "from {} import {}".format(rel_char, name)
            raise ValueError("No valid relative import. Must contain some names for import.")
        elif self.importAll:
            return "from {} import *".format(name, )
        elif self.imports:
            return "from {} import {}".format(name, self.__getImports())
        if name == ".":
            raise SyntaxError("The '.' is not valid for direct import.")
        return 'import {}{}'.format(
            name,
            ' as {}'.format(self.alias) if self.alias else ''
        )
