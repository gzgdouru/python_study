'''
生成器的使用
'''


# 斐波拉契 1 1 2 3 5 8
def fib(n=10):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib2(n=10):
    res_list = []
    a, b = 0, 1
    for i in range(n):
        res_list.append(b)
        a, b = b, a + b
    return res_list


def fib3(n=10):
    a, b = 0, 1
    for i in range(n):
        yield b
        a, b = b, a + b

if __name__ == "__main__":
    for i in fib3():
        print(i, end=" ")