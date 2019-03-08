'''
用于过滤的生成器函数
'''
import itertools


def vowel(c):
    return c.lower() in "aeiou"


if __name__ == "__main__":
    print(list(filter(vowel, "Aardvark")))

    print(list(itertools.filterfalse(vowel, "Aardvark")))

    print(list(itertools.dropwhile(vowel, "Aardvark")))

    print(list(itertools.takewhile(vowel, "Aardvark")))

    print(list(itertools.islice("Aardvark", 4)))
    print(list(itertools.islice("Aardvark", 4, 7)))
    print(list(itertools.islice("Aardvark", 1, 7, 2)))
