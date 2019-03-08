'''
跳过可迭代对象的开始部分
'''
import itertools

if __name__ == "__main__":
    lines = [1, 1, 2, 3, 1, 4, 5]
    for i in itertools.dropwhile(lambda x: x == 1, lines):
        print(i, end=" ")
    print("")