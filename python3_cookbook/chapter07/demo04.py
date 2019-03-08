'''
 返回多个值的函数
'''
def myfun():
    return 1, 2, 3

if __name__ == "__main__":
    a, b, c = myfun()
    print(a, b, c)

    x = myfun()
    print(x)

    x, y, _ = myfun()
    print(x, y)