'''
在查询的时候把非字符串的键转换成字符串
'''
from collections import UserDict


class StrKeyDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, item):
        return item in self.keys() or str(item) in self.keys()


if __name__ == "__main__":
    d = StrKeyDict([("2", "two"), ("4", "four")])
    print(d["2"])
    print(d[4])
    print(d.get(2))
    print(2 in d)
