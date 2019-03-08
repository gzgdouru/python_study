'''
合并多个字典或映射
'''
from collections import ChainMap

if __name__ == "__main__":
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    c = ChainMap(a, b)
    print(c, c["z"])
    del c["z"]
    print(c, c["z"])
    print(a)

    c["x"] = 10
    print(c)
    print(a)