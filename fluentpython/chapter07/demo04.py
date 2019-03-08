'''
一个简单的装饰器
'''
import time
from functools import wraps


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


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == "__main__":
    print("*" * 40, "calling snooze(0.123)")
    snooze(0.123)
    print("*" * 40, "calling factorial(20)")
    print("20! = ", factorial(20))
