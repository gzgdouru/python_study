'''
第4版: 生成器表达式
'''
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return "Sentence({})".format(reprlib.repr(self.text))

    def __str__(self):
        return self.text

    def __iter__(self):
        return (match_obj.group() for match_obj in RE_WORD.finditer(self.text))


if __name__ == "__main__":
    s = Sentence('"The time has come," the Walrus said')
    print(s)

    for word in s:
        print(word, end=" ")
    print("")

    print(list(s))