from ._nameable import Nameable

__all__ = ('PathNode', 'ImportPathNode', 'getFullname', 'nodable')


def getFullname(value):
    if isinstance(value, PathNode):
        return value.fullname
    return str(value)


def _createParentable(name, cls):
    result = object.__new__(cls)
    result.name = name
    result._parent = None
    return result


def nodable(*parts, **kwargs):
    cls = kwargs.get('cls')
    if not cls:
        raise ValueError('`cls` is required')
    if not parts:
        return None

    result = _createParentable(parts[-1], cls)
    parent = None
    for index in range(1, len(parts)):
        it = _createParentable(parts[-index - 1], cls)
        if parent is None:
            parent = result
        parent._parent = it
        parent = parent._parent

    return result


class PathNode(Nameable):
    def __init__(self, name):
        if not isinstance(name, (list, tuple)):
            name = str(name).split(self._sep)
        self._parent = self._fromParts(name[:-1])
        super(PathNode, self).__init__(name[-1])

    _sep = "/"

    @staticmethod
    def normalize(value):
        return getFullname(value).replace(ImportPathNode._sep, PathNode._sep)

    @staticmethod
    def of(value):
        value = PathNode.normalize(value)
        return PathNode(value)

    @staticmethod
    def _fromParts(parts, cls=None):
        if cls is None:
            cls = PathNode
        return nodable(*parts, cls=cls)

    @property
    def parent(self):
        return self._parent

    @property
    def parents(self):
        parent = self.parent
        while parent is not None:
            yield parent
            parent = parent.parent

    @property
    def fullname(self):
        parent = self.parent
        if not parent:
            return self.name
        out = ""
        for parent in self.parents:
            if not out:
                out = parent.name
            else:
                out = "{}{}{}".format(parent.name, self._sep, out)
        if not out:
            return self.name
        return "{}{}{}".format(out, self._sep, self.name)

    def __str__(self):
        return self.fullname


class ImportPathNode(PathNode):
    _sep = "."

    @staticmethod
    def normalize(value):
        return getFullname(value).replace(PathNode._sep, ImportPathNode._sep)

    @staticmethod
    def of(value):
        value = ImportPathNode.normalize(value)
        return ImportPathNode(value)

    @staticmethod
    def _fromParts(parts, cls=None):
        if cls is None:
            cls = ImportPathNode
        return PathNode._fromParts(parts, cls)
