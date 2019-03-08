'''
Vector第五版: 格式化
'''
from array import array
import reprlib
import math
import numbers
import functools
import operator
import itertools


class Vector:
    typecode = "d"
    shortcut_nams = "xyzt"

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
        # if len(self) != len(other):
        #     return False
        #
        # for a, b in zip(self, other):
        #     if a != b:
        #         return False
        #
        # return True
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

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

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_nams.find(name)
            if 0 <= pos < len(cls.shortcut_nams):
                return self._components[pos]
        raise AttributeError(f"{cls.__name__} object has no attribute {name}")

    def __setattr__(self, key, value):
        cls = type(self)
        if len(key) == 1:
            if key in cls.shortcut_nams:
                error = f"readonly attribute {key}"
            elif key.islower():
                error = f"can't set attributes 'a' to 'z' in {cls.__name__}"
            else:
                error = ""

            if error:
                raise AttributeError(error)
        super().__setattr__(key, value)

    def __hash__(self):
        # hashes = (hash(x) for x in self._components)
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, 0)

    @classmethod
    def formbytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, format_spec):
        if format_spec.endswith("h"):
            format_spec = format_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = "<{}>"
        else:
            coords = self
            outer_fmt = "({})"
        componets = (format(c, format_spec) for c in coords)
        return outer_fmt.format(", ".join(componets))


if __name__ == "__main__":
    v = Vector(range(5))
    print(v)

    print(format(v))
    print(format(v, ".5f"))
    print(format(v, ".5fh"))