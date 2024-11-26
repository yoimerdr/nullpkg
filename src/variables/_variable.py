from ..utils import NameTypeIndentable, printable

__all__ = ('Variable',)


class Variable(NameTypeIndentable):
    def __init__(self, name, value=None, level=0, type=None):
        super(Variable, self).__init__(name, level, type)
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = printable(value)

    def __str__(self):
        return "{}{}{} = {}\n".format(
            self.indent,
            self.name,
            '' if not self.type else self.type,
            self.value
        )
