'''
获取终端的大小
'''
import os

if __name__ == "__main__":
    sz = os.get_terminal_size()
    print(sz)
