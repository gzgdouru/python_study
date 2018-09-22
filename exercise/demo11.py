# -*- coding:utf-8 -*-
'''
    1,1,2,3,5,8,13,21....
'''

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def fib2(n):
    f1 = 1
    f2 = 1
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(n - 1):
            f1, f2 = f2, f1 + f2
    return f1

print fib(8)
print fib2(3)