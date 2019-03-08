'''
用于映射的生成器函数
'''
import itertools
import operator

if __name__ == "__main__":
    sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
    print(list(itertools.accumulate(sample)))
    print(list(itertools.accumulate(sample, min)))
    print(list(itertools.accumulate(sample, max)))
    print(list(itertools.accumulate(sample, operator.mul)))
    print(list(itertools.accumulate(range(1, 10), operator.mul)))
    print("-" * 80)

    print(list(enumerate("albatroz", 1)))
    print(list(map(operator.mul, range(11), range(11))))
    print(list(map(operator.mul, range(11), [2, 4, 8])))
    print(list(map(lambda a, b: (a, b), range(11), [2, 4, 8])))
    print("-" * 80)

    print(list(itertools.starmap(operator.mul, enumerate("albatroz", 1))))
    print(list(itertools.starmap(lambda a, b: b / a, enumerate(itertools.accumulate(sample), 1)))) #计算平均值
