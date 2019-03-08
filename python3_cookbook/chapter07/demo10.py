'''
带额外状态信息的回调函数
'''


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


def print_result(result):
    print('Got:', result)


def add(x, y):
    return x + y


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

    return handler


def make_handler_2():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


if __name__ == "__main__":
    # apply_async(add, (2, 3), callback=print_result)
    # apply_async(add, ("hello", "world"), callback=print_result)

    # r = ResultHandler()
    # apply_async(add, (2, 3), callback=r.handler)
    # apply_async(add, ("hello", "world"), callback=r.handler)

    # r = make_handler()
    # apply_async(add, (2, 3), callback=r)
    # apply_async(add, ("hello", "world"), callback=r)

    r = make_handler_2()
    r.send(None)
    apply_async(add, (2, 3), callback=r.send)
    apply_async(add, ("hello", "world"), callback=r.send)
