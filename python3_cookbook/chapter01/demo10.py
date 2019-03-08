'''
删除序列相同元素并保持顺序
'''


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_ex(items, key=None):
    seen = set()
    for item in items:
        val = key(item) if key else item
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == "__main__":
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe_ex(a)))

    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    print(list(dedupe_ex(a, key=lambda s:(s['x'],s['y']))))
