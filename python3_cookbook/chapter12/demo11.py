'''
实现消息发布/订阅模型
'''
from collections import defaultdict
from contextlib import contextmanager


class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)

    @contextmanager
    def subscriber(self, *tasks):
        for task in tasks:
            self.attach(task)

        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)


_exchanges = defaultdict(Exchange)


def get_exchange(name):
    return _exchanges[name]


class DisplayMessages:
    def __init__(self):
        self.count = 0

    def send(self, msg):
        self.count += 1
        print('msg[{}]: {!r}'.format(self.count, msg))


if __name__ == "__main__":
    exc = get_exchange("display_message")
    d1 = DisplayMessages()
    d2 = DisplayMessages()
    with exc.subscriber(d1, d2):
        exc.send("hello")
        exc.send("hi")
