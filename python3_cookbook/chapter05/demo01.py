'''
读写文本数据
'''

if __name__ == "__main__":
    for line in open("demo01.py", encoding="utf-8", errors="replace"):
        print(line.strip())
