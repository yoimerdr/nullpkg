from ._function import Function

__all__ = ('ClassMethod', 'ClassMethodType')


class ClassMethodType:
    STATIC = 'static'
    CLASS = 'class'
    OWN = 'own'


class ClassMethod(Function):
    def __init__(self, name, params=None, level=1, return_value=None, return_type=None, type=ClassMethodType.OWN):
        super(ClassMethod, self).__init__(name, ('self',), level, return_value, return_type)
        self.__is_magic = False
        self.__type = None
        self.type = type
        if params:
            for param in params:
                self.append(param)

    @staticmethod
    def magic(name, params=None,
              level=1, return_value=None, return_type=None):
        param = ClassMethod('__{}__'.format(name), params, level, return_value, return_type)
        param.__is_magic = True

        return param

    @staticmethod
    def init(params=None, level=1, ):
        return ClassMethod.magic('init', params, level)

    @staticmethod
    def str(params=None, level=1, ):
        return ClassMethod.magic('str', params, level)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if self.__type and self.__is_magic:
            raise ValueError("You cannot change the type property for magic methods.")
        self.__type = ClassMethodType.OWN if value not in (ClassMethodType.STATIC, ClassMethodType.CLASS) else value

        param = self.params['self']
        if param:
            if self.__type is ClassMethodType.CLASS:
                param.name = 'cls'
            elif self.__type is ClassMethodType.STATIC:
                self.remove('self')
        elif self.__type is not ClassMethodType.STATIC:
            params = self.params
            self.clear()
            self.append('self')
            if params:
                for param in params:
                    self.append(param)
            if self.__type is not ClassMethodType.OWN:
                self.__type = ClassMethodType.CLASS

    def copy(self):
        met = ClassMethod(
            self.name,
            self.params,
            self.level,
            self.returnValue,
            self.returnType,
            self.type
        )
        met.__is_magic = self.__is_magic

    def __str__(self):
        value = super(ClassMethod, self).__str__()
        decorator = ''
        if self.type is ClassMethodType.STATIC:
            decorator = '@staticmethod'
        elif self.type is ClassMethodType.CLASS:
            decorator = '@classmethod'
        return "{}{}\n{}".format(
            self.indent,
            decorator,
            value
        )
