'''
把输入的各个参数扩展成多个输出元素的生成器函数
'''
import itertools
import operator

if __name__ == "__main__":
    ct = itertools.count()
    print(next(ct), next(ct), next(ct), next(ct))
    print(list(itertools.islice(itertools.count(1, 0.3), 3)))
    cy = itertools.cycle("ABC")
    print(list(itertools.islice(cy, 7)))
    rp = itertools.repeat(7)
    print(next(rp), next(rp))
    print(list(itertools.repeat(8, 4)))
    print(list(map(operator.mul, range(11), itertools.repeat(5))))
    print("-" * 80)

    print(list(itertools.combinations("ABC", 2)))
    print(list(itertools.combinations_with_replacement("ABC", 2)))
    print(list(itertools.permutations("ABC", 2)))
    print(list(itertools.product("ABC", repeat=2)))
