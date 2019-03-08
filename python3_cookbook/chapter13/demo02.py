'''
终止程序并给出错误信息
'''
import sys

if __name__ == "__main__":
    sys.stderr.write("It failed!\n")
    raise SystemExit(1)
    print("hhaha")