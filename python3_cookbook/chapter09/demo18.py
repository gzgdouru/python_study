'''
以编程方式定义类
'''
import types
from operator import itemgetter
import sys


def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    "__init__": __init__,
    'cost': cost,
}
Stock = types.new_class("Stock", (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__


def named_tuple(classname, classfields):
    cls_dict = {name: property(itemgetter(n)) for n, name in enumerate(classfields)}

    def __new__(cls, *args):
        if len(args) != len(classfields):
            raise TypeError('Expected {} arguments'.format(len(classfields)))
        return tuple.__new__(cls, args)


    cls_dict["__new__"] = __new__
    cls = types.new_class(classname, (tuple,), {}, lambda ns:ns.update(cls_dict))
    cls.__module__ = sys._getframe(1).f_globals['__name__']

    return cls

if __name__ == "__main__":
    # s = Stock('ACME', 50, 91.1)
    # print(s.cost())

    Point = named_tuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x, p.y)
    # p.x = 10


