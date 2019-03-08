'''
第4版: 惰性实现
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
        for match_obj in RE_WORD.finditer(self.text):
            yield match_obj.group()


if __name__ == "__main__":
    s = Sentence('"The time has come," the Walrus said')
    print(s)

    for word in s:
        print(word, end=" ")
    print("")

    print(list(s))
