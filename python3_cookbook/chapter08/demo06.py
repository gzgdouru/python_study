'''
创建可管理的属性
'''


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    p = Person("ouru")
    p.first_name = "wancaiji"
    print(p.first_name)

    circle = Circle(4)
    print(circle.radius)
    print(circle.diameter)
    print(circle.perimeter)
    print(circle.area)