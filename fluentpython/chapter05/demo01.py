'''
根据反向拼写给一个单词列表排序
'''


def reverse(word):
    return word[::-1]


if __name__ == "__main__":
    print(reverse("testing"))

    fruits = ["strawberry", "fig", "apple", "cherry", "raspberry", "banana"]
    print(sorted(fruits, key=reverse))
