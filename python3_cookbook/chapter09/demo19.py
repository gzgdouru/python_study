'''
在定义的时候初始化类的成员
'''
from operator import itemgetter


class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(itemgetter(n)))


class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []

    def __new__(cls, *args, **kwargs):
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls, args)


class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']


class Point(StructTuple):
    _fields = ['x', 'y']


if __name__ == "__main__":
    s = Stock('ACME', 50, 91.1)
    print(s.price)
