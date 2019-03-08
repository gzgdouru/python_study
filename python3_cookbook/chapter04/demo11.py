'''
同时迭代多个序列
'''
import itertools

if __name__ == "__main__":
    a = [1, 2, 3]
    b = ['w', 'x', 'y', 'z']
    # for i in zip(a, b):
    #     print(i)

    # for i in itertools.zip_longest(a, b):
    #     print(i)

    print(dict(zip(a, b)))