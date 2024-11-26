__all__ = ('Indentable',)


class Indentable(object):
    indentation = "    "

    def __init__(self, level):
        self.level = level

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        level = 0 if not level else int(level)
        if level < 0:
            level = 0
        self._level = level

    @property
    def indent(self):
        return self.level * self.indentation

    @property
    def nextIndent(self):
        return Indentable(self.level + 1)

    def __str__(self):
        return self.indent
