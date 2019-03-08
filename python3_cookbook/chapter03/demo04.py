'''
二八十六进制整数
'''

if __name__ == "__main__":
    x = 1234
    print(bin(x))
    print(oct(x))
    print(hex(x))

    print(format(x, "b"))
    print(format(x, "o"))
    print(format(x, "x"))

    print(int("4d2", 16))
    print(int("10011010010", 2))

    print(0o755)