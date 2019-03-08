'''
使用属性表示访问json类对象(用__new__方法实现)
'''
from collections import abc
import keyword

from chapter19.demo01 import load


class FrozenJson:
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg


    def __init__(self, mapping):
        self._data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += "_"
            self._data[key] = value

    def __getattr__(self, name):
        if hasattr(self._data, name):
            return getattr(self._data, name)
        else:
            try:
                if keyword.iskeyword(name):
                    name += "_"
                data = self._data[name]
            except KeyError:
                raise AttributeError("")
            else:
                return FrozenJson(data)

if __name__ == "__main__":
    raw_feed = load()
    feed = FrozenJson(raw_feed)
    print(feed.Schedule.speakers)
    print(feed.Schedule.speakers[-1].name)
