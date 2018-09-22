# 任一个英文的纯文本文件，统计其中的单词出现的个数

if __name__ == "__main__":
    filePath = r"F:\git\c2011\random/main.cpp"
    count = 0
    for line in filePath:
        count += len(line.split(" "))

    print(count)
