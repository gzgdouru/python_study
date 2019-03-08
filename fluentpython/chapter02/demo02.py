'''
命名元组的属性和方法
'''
from collections import namedtuple

if __name__ == "__main__":
    City = namedtuple("City", "name country population coordinates")
    tokyo = City("tokyo", "JP", 36.933, (35.689722, 139.691667))
    print(tokyo._fields)
    print(tokyo._asdict())