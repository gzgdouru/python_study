'''
计算整数0到5的累计异或的3中方式
'''
import functools
import operator

if __name__ == "__main__":
    n = 0
    for i in range(1, 6):
        n ^= i
    print(n)

    print(functools.reduce(lambda a, b: a^b, range(6)))
    print(functools.reduce(operator.xor, range(6)))
