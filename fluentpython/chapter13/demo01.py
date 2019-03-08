'''
一元运算符
'''
from array import array
import reprlib
import math
import numbers
import itertools
import numbers


class Vector:
    typecode = "d"

    def __init__(self, iterable):
        self._components = array(self.typecode, iterable)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find("["):-1]
        return "Vector({})".format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes(ord(self.typecode)) + bytes(self._components))

    def __eq__(self, other):
        if isinstance(other, Vector):
            return len(self) == len(other) and all(a == b for a, b in zip(self, other))
        else:
            return NotImplemented

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = "{cls.__name__} indices must be integers"
            raise TypeError(msg.format(cls=cls))

    @classmethod
    def formbytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __neg__(self):
        '''-(取负)'''
        return Vector(-x for x in self)

    def __pos__(self):
        '''+(取正)'''
        return Vector(self)

    def __add__(self, other):
        '''相加'''
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return Vector(n * other for n in self)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other


if __name__ == "__main__":
    v1 = Vector(range(10))
    v2 = Vector(range(10, 15))
    print(v1)
    print(v2)

    print(-v1)
    print(+v1)

    print(v1 + v2)
    print([1, 2, 3] + v1)

    print(14 * v1)

    print(v1 == tuple(range(10)))
    v3 = Vector(range(10))
    print(v1 == v3)

    print(v1 != v3)
    print(v1 != tuple(range(10)))
