from ..utils import NameTypeable, printable

__all__ = ('Parameter',)


class Parameter(NameTypeable):
    def __init__(self, name, value=None, required=False, type=None):
        if isinstance(name, Parameter):
            type = name.type
            name, value, required = name.name, name.value, name.required
        super(Parameter, self).__init__(name, type)
        self.required = required
        self.value = value
        self.type = type

    def _validatename(self, name):
        cl = name.count("*")
        if cl > 2:
            raise SyntaxError("The parameter name is invalid.")
        if cl:
            name = name[cl:]
        super(Parameter, self)._validatename(name)
        if cl:
            name = "{}{}".format("*" * cl, name)
        self.__isVaryingLength = name.startswith('*')
        return name

    @staticmethod
    def args(name='args', type=None):
        return Parameter("*" + name, type=type)

    @staticmethod
    def kwargs(name='kwargs', type=None):
        return Parameter("**" + name, type=type)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = None if value is None and self.required else printable(value)

    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = bool(value)

    @property
    def isVaryingLength(self):
        return self.__isVaryingLength

    def __str__(self):
        value = '{}{}'.format(
            self.name,
            '' if not self.type else str(self.type),
        )

        if self.isVaryingLength or not self.value:
            return value

        return '{} = {}'.format(value, self.value)
