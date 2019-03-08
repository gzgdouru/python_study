'''
字符串的I/O操作
'''
import io

if __name__ == "__main__":
    s = io.StringIO()
    s.write("hello world!\n")
    print("this is test\n", file=s)
    print(s.read(4))
    print("-"*80)
    print(s.getvalue(), end="")
    print("-"*80)


    s = io.StringIO("hello world\n")
    print(s.read(4))
    print(s.read())
