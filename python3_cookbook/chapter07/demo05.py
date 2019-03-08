'''
定义有默认参数的函数
'''
_no_value = object()


def spam(a, b=_no_value):
    if b is _no_value:
        print("No b value supplied")


x = 42


def spam2(a, b=x):
    print(a, b)


def spam3(a, b=[]):
    print(a, b)
    return b


if __name__ == "__main__":
    spam(1, 2)

    spam2(1)
    x = 23
    spam2(1)

    vals = spam3(1)
    vals.append(2)
    vals.append(3)
    spam3(1)
