'''
内存映射的二进制文件
'''
import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


if __name__ == "__main__":
    size = 1000000
    with open('data.bin', 'wb') as f:
        f.seek(size - 1)
        f.write(b'\x00')

    m = memory_map('data.bin')
    print(len(m))
    m[0:11] = b"hello world"
    m.close()

    with memory_map('data.bin') as m:
        print(len(m))
        print(m[0:11])
