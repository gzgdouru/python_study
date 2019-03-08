'''
第2版: 经典的迭代器
'''
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(self.text)

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return "Sentence({})".format(reprlib.repr(self.text))

    def __str__(self):
        return self.text

    def __iter__(self):
        return SentenceIterator(self.words)


if __name__ == "__main__":
    s = Sentence('"The time has come," the Walrus said')
    print(s)

    for word in s:
        print(word, end=" ")
    print("")
    print(list(s))
