'''
在局部变量域中执行代码
'''
from collections import namedtuple


def test():
    a = 13
    loc = locals()
    exec("b = a + 1")
    b = loc["b"]
    print(b)


def test1():
    x = 0
    loc = locals()
    print('before:', loc)
    exec("x += 1")
    print('after:', loc)
    print("x = ", loc["x"])


def test2():
    x = 0
    loc = locals()
    print(loc)
    exec("x += 1")
    print(loc)

    locals()
    print(loc)


def test3():
    a = 13
    loc = {"a": a}
    glb = {}
    exec("b=a+1",loc)
    b = loc["b"]
    print(b)


if __name__ == "__main__":
    test3()
