'''
解除一个装饰器
'''
import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper

@timethis
def add(x, y):
    return x + y


if __name__ == "__main__":
    print(add(1, 3))

    print(add.__wrapped__(1, 3))
