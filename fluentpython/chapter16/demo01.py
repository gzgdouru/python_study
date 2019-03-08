'''
使用协程计算移动平均值
'''


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


if __name__ == "__main__":
    coro_avg = averager()
    print(coro_avg.send(None))
    print(coro_avg.send(10))
    print(coro_avg.send(15))
    print(coro_avg.send(4))
