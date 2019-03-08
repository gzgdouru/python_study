'''
读写JSON数据
'''
import json
from collections import OrderedDict
from pprint import pprint


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x:{self.x} y:{self.y}"


def serialize_instance(obj):
    d = {"__classname__": type(obj).__name__}
    d.update(vars(obj))
    return d


classes = {
    'Point': Point
}


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d


if __name__ == "__main__":
    # data = {
    #     'name': 'ACME',
    #     'shares': 100,
    #     'price': 542.23
    # }
    # json_str = json.dumps(data, indent=4)
    # data = json.loads(json_str)
    # pprint(data)
    # pprint(json.loads(json_str, object_hook=OrderedDict))
    #
    # data = json.loads(json_str, object_hook=JSONObject)
    # print(data.name, data.shares, data.price)

    p = Point(1, 2)
    json_data = json.dumps(p, default=serialize_instance, indent=4)
    print(json_data)

    p = json.loads(json_data, object_hook=unserialize_object)
    print(p)
