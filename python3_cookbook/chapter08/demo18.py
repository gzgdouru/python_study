'''
利用Mixins扩展类功能
'''
from collections import defaultdict


class LoggedMappingMixin:
    __slots__ = ()

    def __getitem__(self, item):
        print('Getting ' + str(item))
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)


class SetOnceMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class StringKeysMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("keys must be strings")
        return super().__setitem__(key, value)


class LoggedDict(LoggedMappingMixin, dict):
    pass


class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass


def LoggedMapping(cls):
    """第二种方式：使用类装饰器"""
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return cls_getitem(self, key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return cls_setitem(self, key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return cls_delitem(self, key)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__
    return cls


@LoggedMapping
class LoggedDict2(dict):
    pass


if __name__ == "__main__":
    # d = LoggedDict()
    # d["x"] = 23
    # print(d["x"])
    # del d["x"]

    # d = SetOnceDefaultDict(list)
    # d["x"].append(2)
    # d["x"].append(3)
    # print(d["x"])
    # # d["x"] = 23

    d = LoggedDict2()
    d["x"] = 23
    print(d["x"])
    del d["x"]
