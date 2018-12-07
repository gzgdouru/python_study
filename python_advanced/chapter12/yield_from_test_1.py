'''
yield详解1
'''


def g1(iterable):
    yield iterable


def g2(iterable):
    yield from iterable


def my_chain(*args, **kwargs):
    for iterable in args:
        yield from iterable

if __name__ == "__main__":
    # for val in g1([1, 2, 3, 4, 5, 6, 7, 8]):
    #     print(val)

    for val in my_chain([1, 2, 3], {"key1":1, "key2":2}, (4, 5, 6)):
        print(val)

