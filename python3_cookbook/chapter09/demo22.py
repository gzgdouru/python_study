'''
定义上下文管理器的简单方法
'''
import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working


if __name__ == "__main__":
    # with timethis("counting"):
    #     n = 10000000
    #     while n > 0:
    #         n -= 1

    items = [1, 2, 3, 4]
    with list_transaction(items) as working:
        working.append(5)
        working.append(6)
        # raise RuntimeError("test")
    print(items)
