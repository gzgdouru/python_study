'''
复制或者移动文件和目录
'''
import shutil

if __name__ == "__main__":
    # shutil.copy("demo06.py", "demo06_bk.py")
    # shutil.copy2("demo06.py", "demo06_bk.py")
    # shutil.copytree("../chapter12", "chapter12_bk")
    # shutil.move("../chapter12", "../chapter12_bk")

    shutil.copytree("../chapter12", "../chapter12_bk", ignore=shutil.ignore_patterns("*.py"))


