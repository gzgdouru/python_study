'''
读写字节数据
'''

if __name__ == "__main__":
    with open("test.bin", "wb") as f:
        f.write("hello world!".encode("utf-8"))

    for line in open("test.bin", "rb"):
        print(line.strip())
