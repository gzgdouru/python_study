'''
使用生成器创建新的迭代模式
'''

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


if __name__ == "__main__":
    for n in frange(0, 10, 0.2):
        print("{:.1f}".format(n))