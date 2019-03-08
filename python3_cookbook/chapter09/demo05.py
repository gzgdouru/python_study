'''
可自定义属性的装饰器
'''
from functools import wraps, partial
import logging


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper

    return decorate


@logged(logging.INFO)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    # print(add(2, 4))
    #
    # add.set_level(logging.ERROR)
    # print(add(2, 3))
    #
    # add.set_message("add called")
    # print(add(2, 5))

    import requests
    response = requests.get(r'http://localhost:8000/context/', headers={"USER-AGENT":"scrap"})
    print(response.status_code)
    print(response.text)
