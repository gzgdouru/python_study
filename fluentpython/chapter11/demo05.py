'''
子类化内置类型很麻烦
'''
import collections

# class DoppelDict(dict):
class DoppelDict(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


# class AnswerDict(dict):
class AnswerDict(collections.UserDict):
    def __getitem__(self, item):
        return 42


if __name__ == "__main__":
    dd = DoppelDict(one=1)
    print(dd)

    dd["two"] = 2
    print(dd)

    dd.update(three=3)
    print(dd)

    print("-" * 80)

    ad = AnswerDict(a="foo")
    print(ad["a"])
    d = {}
    d.update(ad)
    print(d["a"])
