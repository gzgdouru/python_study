'''
增量赋值运算符
'''
import abc
import random


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        pass

    @abc.abstractmethod
    def pick(self):
        pass

    @abc.abstractmethod
    def loaded(self):
        return bool(self.inspect)

    @abc.abstractmethod
    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty BingoCage")

    def loaded(self):
        return super().loaded()

    def inspect(self):
        return super().inspect()

    def __call__(self, *args, **kwargs):
        return self.pick()


class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError("pick from empty LotteryBlower")
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))


@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError("pop from empty TomboList")

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


class AddableBingoCage(BingoCage):
    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()
        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                cls_name = type(self).__name__
                raise TypeError("right operand in += must be {} or a iterable".format(cls_name))

        self.load(other_iterable)
        return self


if __name__ == "__main__":
    vowels = "AEIOU"
    globe = AddableBingoCage(vowels)
    print(globe.inspect())
    globe2 = AddableBingoCage("ZXY")
    globe3 = globe + globe2
    print(globe3.inspect())

    globe_orig = globe
    globe_orig += globe2
    print(globe_orig.inspect())
    globe_orig += ["M", "N"]
    print(globe_orig.inspect())