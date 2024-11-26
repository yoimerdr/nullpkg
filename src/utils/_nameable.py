import re

__all__ = ('KEYWORDS', 'getName', 'Nameable')

KEYWORDS = (
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del',
    'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
    'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
)


def getName(nameable):
    if isinstance(nameable, Nameable):
        return nameable.name
    return str(nameable)


class Nameable(object):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is None:
            raise ValueError('Name cannot be none.')
        if isinstance(name, Nameable):
            self._name = name.name
            return

        name = str(name).strip()
        if not name:
            raise ValueError('Name cannot be empty: {}.'.format(name))
        name = self._validatename(name)
        if name in KEYWORDS:
            raise SyntaxError('Name cannot be a keyword: {}.'.format(name))
        self._name = name

    def _validatename(self, name):
        if not re.match(r'^[_A-Za-z]+\w*?$', name):
            raise SyntaxError("Name must be a valid variables name: {}.".format(name))
        return name

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)
