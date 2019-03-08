'''
字典排序
'''
from collections import OrderedDict

if __name__ == "__main__":
    d = {}
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    d['bae'] = 6
    print(d)

    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    print(d)