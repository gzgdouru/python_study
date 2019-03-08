'''
实现数据模型的类型约束
'''


class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)


class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super().__set__(instance, value)


class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


class checkedmeta(type):
    def __new__(cls, class_name, class_parent, class_attr, **kwargs):
        for key, value in class_attr.items():
            if isinstance(value, Descriptor):
                value.name = key

        return super().__new__(cls, class_name, class_parent, class_attr, **kwargs)


def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls

    return decorate


class Base:
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class Stock1(Base):
    name = SizedString('name', size=8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')


class Stock2(Base, metaclass=checkedmeta):
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()


@check_attributes(name=SizedString(size=8),
                  shares=UnsignedInteger,
                  price=UnsignedFloat)
class Stock3(Base):
    pass


if __name__ == "__main__":
    s = Stock3(name="ACME", shares=75, price=4.5)
    print(s.__dict__)
