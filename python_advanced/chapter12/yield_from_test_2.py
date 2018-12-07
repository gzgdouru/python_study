from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break  # 为了返回值，协程必须正常终止；这里是退出条件
        total += term
        count += 1
        average = total / count
    # 返回一个namedtuple，包含count和average两个字段。在python3.3前，如果生成器返回值，会报错
    return Result(count, average)


final_result = None


def middle():
    while True:
        global final_result
        final_result = yield from averager()


def main():
    nums = [10, 20, 30, 40, 50]
    m = middle()
    m.send(None)  # 激活生成器
    for num in nums:
        m.send(num)
    m.send(None)  # 结束生成器
    print(final_result)


if __name__ == "__main__":
    # gen = averager()
    # gen.send(None)
    # gen.send(20)
    # gen.send(30)
    # try:
    #     print(gen.send(None))
    # except StopIteration as e:
    #     print(e.value)

    main()
