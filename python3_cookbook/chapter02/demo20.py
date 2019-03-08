'''
字节字符串上的字符串操作
'''
import re

if __name__ == "__main__":
    data = b'Hello World'
    print(data[0:5])
    print(data.startswith(b"Hello"))
    print(data.split(b" "))
    print(data.replace(b'Hello', b'Hello Cruel'))

    data = b'FOO:BAR,SPAM'
    print(re.split(br'[,:]', data))

    b = b'Hello World'
    print(b[0])
    print(chr(b[0]))