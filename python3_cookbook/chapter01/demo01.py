'''
解压序列赋值给多个变量
'''

if __name__ == "__main__":
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    print(name, shares, price, date)

    name, shares, price, (year, month, day) = data
    print(name, shares, price, year, month, day)

    s = "hello"
    a, b, c, d, e = s
    print(a, b, c, d, e)

    name, _, price, _ = data
    print(name, price)
