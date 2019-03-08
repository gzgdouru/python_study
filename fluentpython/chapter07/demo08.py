'''
参数化clock装饰器
'''
import time
from functools import partial

DEFAULT_FMT = "[{elapsed:0.8f}s] {name}({args}) -> {result}"


def clock(func=None, *, fmt=DEFAULT_FMT):
    if func is None:
        return partial(clock, fmt=fmt)

    # def decorate(func):
    def clocked(*_args):
        t0 = time.time()
        _result = func(*_args)
        elapsed = time.time() - t0
        name = func.__name__
        args = ", ".join(str(arg) for arg in _args)
        result = str(_result)
        print(fmt.format(**locals()))
        return _result

    return clocked

    # return decorate


# @clock
@clock(fmt="{name}: {elapsed}")
def snooze(seconds):
    time.sleep(seconds)


if __name__ == "__main__":
    for i in range(3):
        snooze(0.123)
