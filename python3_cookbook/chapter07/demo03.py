'''
给函数参数增加元信息
'''


def add(x: int, y: int) -> int:
    return x + y

if __name__ == "__main__":
    print(add(4, 5))
    print(help(add))
