'''
字典的运算
'''

if __name__ == "__main__":
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    min_price = min(zip(prices.values(), prices.keys()))
    print(min_price)
    max_price = max(zip(prices.values(), prices.keys()))
    print(max_price)

    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    print(prices_sorted)

    min_key = min(prices, key=lambda s:prices[s])
    print(min_key, prices[min_key])
