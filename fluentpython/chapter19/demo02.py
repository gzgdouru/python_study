'''
使用属性表示访问json类对象
'''
from collections import abc
import keyword

from chapter19.demo01 import load


class FrozenJson:
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
                return FrozenJson.build(data)

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


if __name__ == "__main__":
    raw_feed = load()
    feed = FrozenJson(raw_feed)
    print(feed.Schedule.speakers[-1].name)
