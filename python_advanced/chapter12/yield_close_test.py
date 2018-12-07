'''
yield中close函数使用
'''


def get_value():
    try:
        yield 1
    except GeneratorExit:
        # GeneratorExit是继承自BaseException
        raise StopIteration()
    yield 2
    yield 3
    return "bobby"


if __name__ == "__main__":
    gen = get_value()
    print(next(gen))
    gen.close()
    print(next(gen))

    print(next(gen))
