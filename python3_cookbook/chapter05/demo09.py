'''
读取二进制数据到可变缓冲区中
'''
import os


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, "rb") as f:
        f.readinto(buf)
    return buf


if __name__ == "__main__":
    with open('sample.bin', 'wb') as f:
        f.write(b'Hello World')
    buf = read_into_buffer("sample.bin")
    buf[0:5] = b"hello"
    with open('newsample.bin', 'wb') as f:
        f.write(buf)
