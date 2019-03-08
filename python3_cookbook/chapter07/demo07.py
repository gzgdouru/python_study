'''
匿名函数捕获变量值
'''

if __name__ == "__main__":
    x = 10
    a = lambda y: x + y
    x = 20
    b = lambda y: x + y
    print(a(10), b(10))

    x = 10
    a = lambda y, x=x: x + y
    x = 20
    b = lambda y, x=x: x + y
    print(a(10), b(10))

    funcs = [lambda x: x + n for n in range(5)]
    for func in funcs:
        print(func(0), end=" ")
    print("")

    funcs = [lambda x, n=n: x + n for n in range(5)]
    for func in funcs:
        print(func(0), end=" ")
