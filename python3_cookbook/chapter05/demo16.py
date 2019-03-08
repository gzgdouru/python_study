'''
增加或改变已打开文件的编码
'''
import io

if __name__ == "__main__":
    with open("demo02.py", encoding="utf-8") as f:
        # content = f.read()
        # print(content)

        f = io.TextIOWrapper(f.detach(), encoding="latin-1")
        content2 = f.read()
        print(content2)