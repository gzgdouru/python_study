'''
迭代器代替while无限循环
'''
import sys

if __name__ == "__main__":
    with open("demo02.py", encoding="utf-8") as f:
        for chunk in iter(lambda :f.read(10), ''):
            sys.stdout.write(chunk)