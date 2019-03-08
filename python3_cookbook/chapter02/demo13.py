'''
字符串对齐
'''

if __name__ == "__main__":
    text = 'Hello World'
    print(repr(text.ljust(20)))
    print(repr(text.rjust(20)))
    print(repr(text.center(20)))

    print(text.ljust(20, "="))
    print(text.center(20, "*"))

    print(repr(format(text, "<20")))
    print(repr(format(text, '>20')))
    print(repr(format(text, "^20")))

    