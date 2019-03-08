'''
第一版:单词序列
'''
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(self.text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return "Sentence({})".format(reprlib.repr(self.text))

    def __str__(self):
        return self.text


if __name__ == "__main__":
    s = Sentence('"The time has come," the Walrus said')
    print(s)

    for word in s:
        print(word, end=" ")
    print("")
    print(list(s))