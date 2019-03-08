'''
使用元类控制实例的创建
'''
import weakref


class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam.grok')


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self._instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance


class Spam2(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cache = weakref.WeakValueDictionary()

    def __call__(self, *args, **kwargs):
        name = kwargs.get("name")
        if args in self._cache:
            return self._cache[name]
        else:
            obj = super().__call__(*args, **kwargs)
            self._cache[name] = obj
            return obj


class Spam3(metaclass=Cached):
    def __init__(self, *, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name


if __name__ == "__main__":
    # Spam.grok(1)
    # spam = Spam()

    # a = Spam2()
    # b = Spam2()
    # print(a is b)

    a = Spam3(name="python")
