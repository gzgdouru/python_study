'''
展开嵌套的序列
'''
from collections import Iterable


def flatten(iterable, ignore_types=(str, bytes)):
    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item, ignore_types):
            yield from flatten(item)
        else:
            yield item


if __name__ == "__main__":
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    for i in flatten(items):
        print(i, end=" ")
    print("")

    items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    for i in flatten(items):
        print(i, end=" ")
    print("")
