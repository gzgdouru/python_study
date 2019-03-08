'''
使用itertools模块生成等差数列
'''
import itertools


def atirprog(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen

if __name__ == "__main__":
    ap = atirprog(0, 1, 3)
    print(list(ap))

    ap = atirprog(0, 0.5, 3)
    print(list(ap))

    from decimal import Decimal

    ap = atirprog(0, Decimal("0.1"), 0.3)
    print(list(ap))

