'''
减少可调用对象的参数个数
'''
from functools import partial


def spam(a, b, c, d):
    print(a, b, c, d)


if __name__ == "__main__":
    func = partial(spam, 1)
    func(2, 3, 4)
    func(4, 5, 6)

    func2 = partial(spam, d=42)
    func2(1, 2, 3)

    func3 = partial(spam, 1, 2, d=42)
    func3(11)