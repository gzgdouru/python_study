'''
字典中的键映射多个值
'''
from collections import defaultdict

if __name__ == "__main__":
    d = defaultdict(list)
    d["a"].append(1)
    d["a"].append(2)
    d["b"].append(4)
    print(d)

    d = {}
    d.setdefault("a", []).append(1)
    d.setdefault("a", []).append(2)
    d.setdefault("b", []).append(4)
    print(d)
