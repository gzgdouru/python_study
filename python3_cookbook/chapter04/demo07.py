'''
迭代器切片
'''
import itertools

def count(n):
    while True:
        yield n
        n += 1

if __name__ == "__main__":
    c = count(0)
    # print(c[:10])
    for i in itertools.islice(c, 10, 20):
        print(i, end=" ")
    print("")
