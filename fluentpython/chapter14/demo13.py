'''
用于重新排列元素的生成器
'''
import itertools

if __name__ == "__main__":
    print(list(itertools.groupby("LLLLAAGGG")))
    for char, group in itertools.groupby("LLLLAAGGG"):
        print(char, list(group))

    animals = ["duck", "eagle", "rat", "giraffe", "bear", "bat", "dolphin", "shark", "lion"]
    animals.sort(key=len)
    for length, group in itertools.groupby(animals, key=len):
        print(length, list(group))

    for length, group in itertools.groupby(reversed(animals), key=len):
        print(length, list(group))

    g1, g2 = itertools.tee("ABC")
    print(next(g1))
    print(next(g1))
    print(next(g2))
    print(list(g1), list(g2))
