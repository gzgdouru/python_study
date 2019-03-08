'''
创建从一个单词到其出现情况的映射
'''
import re

RE_WORD = re.compile(r'\w+')
index = {}

if __name__ == "__main__":
    with open("demo01.py", encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            for match in RE_WORD.finditer(line):
                word = match.group()
                column_no = match.start()+1
                location = (lineno, column_no)
                index.setdefault(word, []).append(location)


    for word in sorted(index, key=str.upper):
        print(word, index[word])
