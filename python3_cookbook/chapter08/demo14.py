'''
实现自定义容器
'''
import bisect
from collections import Sequence, MutableSequence


class SortedItems(Sequence):
    def __init__(self, initial=None):
        self._initial = sorted(initial) if initial is not None else []

    def __getitem__(self, item):
        return self._initial[item]

    def __len__(self):
        return len(self._initial)

    def add(self, item):
        bisect.insort(self._initial, item)


class Items(MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value

    def __delitem__(self, index):
        print('Deleting:', index)
        del self._items[index]

    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)


if __name__ == "__main__":
    # items = SortedItems([5, 1, 3])
    # print(list(items))
    # items.add(2)
    # print(list(items))

    items = Items([5, 1, 3])
    print(list(items))


