'''
通过文件名查找文件
'''
import os


def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))


if __name__ == "__main__":
    findfile("f:/", "demo02.py")
