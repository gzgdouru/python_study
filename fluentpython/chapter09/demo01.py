'''
向量类
'''
from array import array
import math
import copy


class Vector2d:
    __slots__ = ("__x", "__y")
    typecode = "d"

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, self.x, self.y)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, format_spec=""):
        if format_spec.endswith("p"):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            out_fmt = "<{}, {}>"
        else:
            coords = self
            out_fmt = "({}, {})"
        compoents = (format(c, format_spec) for c in coords)
        return out_fmt.format(*compoents)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def angle(self):
        return math.atan2(self.y, self.x)


if __name__ == "__main__":
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)

    x, y = v1
    print(x, y)

    print(repr(v1))
    print(v1)

    octets = bytes(v1)
    print(octets)

    v2 = copy.copy(v1)
    print(v1 == v2)

    print(abs(v1))

    v3 = Vector2d(0, 0)
    print(bool(v3))

    v4 = Vector2d.frombytes(octets)
    print(v4)

    print(format(v1))
    print(format(v1, ".2f"))
    print(format(v1, ".3e"))

    print(format(v1, "p"))
    print(format(v1, ".2fp"))

    print(hash(v1))
