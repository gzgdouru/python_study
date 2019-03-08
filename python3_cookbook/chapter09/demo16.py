'''
 *args和**kwargs的强制参数签名
'''
from inspect import Signature, Parameter

parms = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
         Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
         Parameter('z', Parameter.KEYWORD_ONLY, default=None)]
sig = Signature(parms)


# print(sig)

def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)


def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(parms)


class Structure:
    __signature__ = make_sig()

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')


class Point(Structure):
    __signature__ = make_sig('x', 'y')


class StructureMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsdict['__signature__'] = make_sig(*clsdict.get("_fields", []))
        return super().__new__(cls, clsname, bases, clsdict)


class Structure2(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock2(Structure2):
    _fields = ('name', 'shares', 'price')


class Point2(Structure2):
    _fields = ('x', 'y')


if __name__ == "__main__":
    # func(1, 2, z=3)
    # func(1, z=3)
    # func(y=2, x=1)
    # func(1, 2, 3, 4)

    # s1 = Stock('ACME', 100, 490.1)
    # s2 = Stock('ACME', 100)

    s1 = Stock2('ACME', 100, 490.1)
    s2 = Stock2('ACME', 100)
