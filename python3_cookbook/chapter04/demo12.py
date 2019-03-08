'''
不同集合上元素的迭代
'''
import itertools

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    b = ['x', 'y', 'z']
    for x in itertools.chain(a, b):
        print(x, end=" ")
    print("")