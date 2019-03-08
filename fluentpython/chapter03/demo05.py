'''
不可变的映射类型
'''
from types import MappingProxyType

if __name__ == "__main__":
    d = {1: 'A'}
    d_proxy = MappingProxyType(d)
    print(d_proxy[1])

    # d_proxy[1] = 10
    d[2] = "B"
    print(d_proxy)