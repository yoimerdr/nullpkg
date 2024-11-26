from ..utils import NameIndentable, getName, to, printable, ReturnType
from ..variables import Parameter

__all__ = ('Function', )


class Function(NameIndentable):
    def __init__(self, name, params=None, level=0, return_value=None, return_type=None, ):
        super(Function, self).__init__(name, level)
        self.params = params
        self.returnType = return_type
        self.returnValue = return_value

    @property
    def params(self):
        return self.__params

    @params.setter
    def params(self, params):
        self.__params = {getName(i): to(i, Parameter, required=True) for i in params} if params else None

    def append(self, param):
        self.__params[getName(param)] = to(param, Parameter, required=True)

    def remove(self, param):
        self.__params.pop(getName(param))

    def clear(self):
        self.__params.clear()

    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, return_type):
        self.__returnType = None if return_type is None else to(return_type, ReturnType)

    @property
    def returnValue(self):
        return self.__returnValue

    @returnValue.setter
    def returnValue(self, value):
        self.__returnValue = None if value is None else printable(value)

    def __str__(self):
        opts = {'non-required': False}

        def checkParam(param):
            if param.required and opts['non-required']:
                raise SyntaxError(
                    "The required parameter '{}' of the function '{}' must be before non-required parameters.".format(
                        param.name, self.name
                    )
                )
            elif not param.required:
                opts['non-required'] = True

            return str(param)

        return "{}def {}({}){}: {}\n".format(
            self.indent,
            self.name,
            ', '.join(map(checkParam, self.params.values())) if self.params else '',
            '' if not self.returnType else ' {}'.format(self.returnType),
            "pass" if not self.returnValue else "return {}".format(self.returnValue),
        )
