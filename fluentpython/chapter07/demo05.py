'''
使用functool.lru_cache做备忘
'''
import time
from functools import wraps, lru_cache


def clock(func):
    @wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_list = [", ".join(str(arg) for arg in args)]
        pairs = ["%s=%r" % (key, val) for key, val in kwargs.items()]
        arg_list.append(", ".join(pairs))
        arg_str = ", ".join(arg_list)
        print("[{:.8}s] {}({}) -> {}".format(elapsed, name, arg_str, result))
        return result

    return clocked


@lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == "__main__":
    print(fibonacci(30))
