'''
使用延迟计算属性
'''
import math


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


def lazyproperty_ex(func):
    name = '_lazy_' + func.__name__

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value

    return lazy


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    c = Circle(4)
    print(c.__dict__)
    print(c.area)
    print(c.__dict__)
    print(c.area)

    print(c.perimeter)
    print(c.__dict__)
    print(c.perimeter)
