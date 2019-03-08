'''
删除字符串中不需要的字符
'''
import re

if __name__ == "__main__":
    s = ' hello world \n'
    print(repr(s))
    print(repr(s.strip()))

    t = '-----hello====='
    print(t.lstrip("-"))
    print(t.strip("-="))

    s = ' hello     world \n'
    print(s.strip())
    print(s.replace(' ', ""))
    print(re.sub(r'\s+', ' ', s))