'''
文件不存在才能写入
'''

if __name__ == "__main__":
    with open("test.txt", "x", encoding="utf-8") as f:
        f.write("hello world!")