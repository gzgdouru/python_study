'''
将装饰器定义为类的一部分
'''
from functools import wraps


class A:
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)

        return wrapper

    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)

        return wrapper

a = A()
@a.decorator1
def spam():
    pass
# As a class method
@A.decorator2
def grok():
    pass

if __name__ == "__main__":
    spam()
    grok()