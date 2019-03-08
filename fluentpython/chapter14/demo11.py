'''
合并多个可迭代对象的生成器函数
'''
import itertools

if __name__ == "__main__":
    print(list(itertools.chain("ABC", range(2))))
    print(list(itertools.chain(enumerate("ABC"))))
    print(list(itertools.chain.from_iterable(enumerate("ABC"))))
    print("-" * 80)

    print(list(zip("ABC", range(5))))
    print(list(zip("ABC", range(5), [10, 20, 30, 40])))
    print(list(itertools.zip_longest("ABC", range(5))))
    print(list(itertools.zip_longest("ABC", range(5), [10, 20, 30, 40], fillvalue="?")))
    print("-" * 80)

    print(list(itertools.product("ABC", range(2))))
    suits = "spads hearts diamonds clubs".split()
    print(list(itertools.product("AK", suits)))
    print(list(itertools.product("ABC")))
    print(list(itertools.product("ABC", repeat=2)))
    print(list(itertools.product(range(2), repeat=3)))
    rows = itertools.product("AB", range(2), repeat=2)
    for row in rows:
        print(row)