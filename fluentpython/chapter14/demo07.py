'''
等差数列生成器
'''


class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index


if __name__ == "__main__":
    ap = ArithmeticProgression(0, 1, 3)
    print(list(ap))

    ap = ArithmeticProgression(0, 0.5, 3)
    print(list(ap))

    from decimal import Decimal

    ap = ArithmeticProgression(0, Decimal("0.1"), 0.3)
    print(list(ap))

    ap = aritprog_gen(0, 1, 3)
    print(list(ap))
