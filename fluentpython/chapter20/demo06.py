'''
方法是描述符
'''
import collections


class Text(collections.UserString):
    def __str__(self):
        return "Text('{}')".format(self.data)

    def reverse(self):
        return self[::-1]



if __name__ == "__main__":
    word = Text("forward")
    print(word)
    print(word.reverse())
    print(Text.reverse(Text("backward")))
    print(type(word.reverse), type(Text.reverse))
    print(list(map(Text.reverse, ["repaid", (10, 20, 30), Text("stressed")])))
    print(Text.reverse.__get__(word))
    print(Text.reverse.__get__(None, Text))
    print(word.reverse)
    print(word.reverse.__self__)
    print(word.reverse.__func__)


