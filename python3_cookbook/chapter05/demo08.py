'''
固定大小记录的文件迭代
'''
from functools import partial


def read_big_file(file, size=10240, delimiter="\n"):
    '''大文件读取'''
    buf = ""
    with open(file, encoding="utf-8") as f:
        for r in iter(partial(f.read, size), ''):
            buf += r
            while delimiter in buf:
                pos = buf.index(delimiter)
                yield buf[:pos]
                buf = buf[pos + len(delimiter):]
        yield buf


if __name__ == "__main__":
    # RECORD_SIZE = 32
    # with open("demo02.py", encoding="utf-8") as f:
    #     records = iter(partial(f.read, RECORD_SIZE), '')
    #     for r in records:
    #         print(r, end="")

    for r in read_big_file("demo08.py"):
        print(r)
