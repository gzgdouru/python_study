'''
定义并使用一个抽象基类
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


if __name__ == "__main__":
    # bingo = BingoCage(range(10))
    # print(bingo())

    # lottery = LotteryBlower(range(10))
    # print(lottery.pick())

    print(issubclass(TomboList, Tombola))
    t = TomboList(range(10))
    print(isinstance(t, Tombola))
