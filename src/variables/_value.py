__all__ = ("Value",)


class Value:
    def __init__(self, value):
        self.__type = 'direct'
        self.__char = '"'
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @staticmethod
    def callable(value):
        value = Value(value)
        value.__type = 'callable'
        return value

    @staticmethod
    def str(value, char='"'):
        value = Value(value)
        value.__char = char
        value.__type = 'str'
        return value

    def __str__(self):
        value = self.value
        if self.__type == 'str':
            value = '{}{}{}'.format(self.__char, value, self.__char)
        elif self.__type == 'callable':
            value = value + '()'
        else:
            value = str(value)
        return value
