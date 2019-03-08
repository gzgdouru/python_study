'''
映射名称到序列元素
'''
from collections import namedtuple

if __name__ == "__main__":
    Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    sub = Subscriber('jonesy@example.com', '2012-10-19')
    print(sub)

    addr, joined = sub
    print(addr, joined)

    # sub.joined = "2018-12-25"
    sub = sub._replace(joined="2018-12-25")
    print(sub)

    Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
    stock_prototype = Stock('', 0, 0.0, None, None)
    a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
    stock = stock_prototype._replace(**a)
    print(stock)