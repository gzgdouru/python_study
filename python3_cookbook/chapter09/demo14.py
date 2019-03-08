'''
 捕获类的属性定义顺序
'''
from collections import OrderedDict


class Typed:
    _expected_type = type(None)

    def __init__(self, name=None):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError(self._name + ' Expected ' + str(self._expected_type))
        instance.__dict__[self.name] = value


class Integer(Typed):
    _expected_type = int


class Float(Typed):
    _expected_type = float


class String(Typed):
    _expected_type = str


class OrderedMeta(type):
    def __new__(cls, clsname, class_parent, class_attr, **kwargs):
        d = dict(class_attr)
        order = []
        for name, value in class_attr.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d["_order"] = order
        return super().__new__(cls, clsname, class_parent, d, **kwargs)

    @classmethod
    def __prepare__(metacls, name, bases):
        return OrderedDict()


class Structure(metaclass=OrderedMeta):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_csv(self):
        return ','.join(str(getattr(self, name)) for name in self._order)


class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()

    # def __init__(self, name, shares, price):
    #     self.name = name
    #     self.shares = shares
    #     self.price = price


if __name__ == "__main__":
    s = Stock(name='GOOG', shares=100, price=490.1)
    print(s.as_csv())
    t = Stock(name='AAPL', shares='a lot', price=610.23)
    t.as_csv()
