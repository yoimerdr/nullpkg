__all__ = ('to', 'printable')


def to(value, cls, copy=False, **kwargs):
    if isinstance(value, cls):
        return value if not copy else cls(value, **kwargs)
    return cls(value, **kwargs)


def printable(value):
    if isinstance(value, str):
        value = '"{}"'.format(value)
    elif value is None:
        value = 'None'

    return value
