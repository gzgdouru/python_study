'''
测试文件是否存在
'''
import os

if __name__ == "__main__":
    print(os.path.exists("demo02.py"))

    print(os.path.isfile("demo02.py"))

    print(os.path.isdir("demo02.py"))

    print(os.path.islink("demo02.py"))
    print(os.path.realpath("demo02.py"))

    print(os.path.getsize("demo02.py"))
    import time
    print(time.ctime(os.path.getmtime("demo02.py")))