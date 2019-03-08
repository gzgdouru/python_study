'''
命名切片
'''

if __name__ == "__main__":
    record = '....................100 .......513.25 ..........'
    SHARES = slice(20, 23)
    PRICE = slice(31, 37)
    cost = int(record[SHARES]) * float(record[PRICE])
    print(cost)

    a = slice(5, 50, 2)
    print(a.start, a.stop, a.step)

    s = "HelloWorld"
    print(a.indices(len(s)))
    for i in range(*a.indices(len(s))):
        print(s[i])