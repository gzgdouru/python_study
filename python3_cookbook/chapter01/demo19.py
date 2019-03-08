'''
转换并同时计算数据
'''

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    total = sum(x * x for x in nums)
    print(total)

    s = ('ACME', 50, 123.45)
    print(",".join(str(x) for x in s))

    portfolio = [
        {'name': 'GOOG', 'shares': 50},
        {'name': 'YHOO', 'shares': 75},
        {'name': 'AOL', 'shares': 20},
        {'name': 'SCOX', 'shares': 65}
    ]
    min_shares = min(s['shares'] for s in portfolio)
    print(min_shares)