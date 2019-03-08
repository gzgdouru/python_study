'''
将字节写入文本文件
'''
import sys

if __name__ == "__main__":
    # sys.stdout.write(b"hello world!")
    sys.stdout.buffer.write(b"hello world!")
    print("")

    with open("test.txt", "w") as f:
        # f.write(b"hahahh!")
        print(f.buffer.write(b"hahha"))