'''
序列上索引值迭代
'''
from collections import defaultdict

if __name__ == "__main__":
    my_list = ['a', 'b', 'c']
    # for idx, val in enumerate(my_list, 1):
    #     print(idx, val)

    word_summary = defaultdict(list)
    with open("demo02.py", encoding="utf-8") as f:
        lines = f.readlines()

    for idx, line in enumerate(lines):
        words = [w.strip().lower() for w in line.split()]
        for word in words:
            word_summary[word].append(idx)

    print(word_summary)


