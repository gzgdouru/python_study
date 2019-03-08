'''
创建缓存实例
'''
import logging
import weakref


class Spam:
    def __init__(self, name):
        self.name = name


_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s


class Spam2:
    def __init__(self):
        raise RuntimeError("Can't instantiate directly")

    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self


class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            tmp = Spam2._new(name)
            self._cache[name] = tmp
        else:
            tmp = self._cache[name]
        return tmp


if __name__ == "__main__":
    # a = logging.getLogger("foo")
    # b = logging.getLogger("bar")
    # c = logging.getLogger("foo")
    # print(a is b)
    # print(a is c)

    # a = get_spam("foo")
    # b = get_spam("bar")
    # c = get_spam("foo")
    # print(a is b)
    # print(a is c)

    cache = CachedSpamManager()
    a = cache.get_spam("foo")
    b = cache.get_spam("bar")
    c = cache.get_spam("foo")
    print(a is b)
    print(a is c)