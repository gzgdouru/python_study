'''
排列组合的迭代
'''
import itertools

if __name__ == "__main__":
    items = ['a', 'b', 'c']
    # for p in itertools.permutations(items, 3):
    #     print(p)

    # for p in itertools.combinations(items, 2):
    #     print(p)


    for p in itertools.combinations_with_replacement(items, 2):
        print(p)
