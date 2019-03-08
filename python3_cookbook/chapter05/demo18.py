'''
将文件描述符包装成文件对象
'''
import os
import sys

if __name__ == "__main__":
    # fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)
    # f = open(fd, "w")
    # f.write("hello world\n")
    # f.close()

    bstdout = open(sys.stdout.fileno(), "wb", closefd=False)
    bstdout.write(b"hello")
    bstdout.flush()
