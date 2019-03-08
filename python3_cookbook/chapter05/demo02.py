'''
打印输出至文件中
'''

if __name__ == "__main__":
    with open("test.txt", "w", encoding="utf-8") as f:
        print("hello world!", file=f)