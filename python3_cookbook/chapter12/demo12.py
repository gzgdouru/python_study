'''
使用生成器代替线程
'''
from collections import deque


def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield
        n -= 1
    print('Blastoff!')


def countup(n):
    x = 0
    while x < n:
        print('Counting up', x)
        yield
        x += 1


class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):
        self._task_queue.append(task)

    def run(self):
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                next(task)
                self.new_task(task)
            except StopIteration:
                pass


class ActorScheduler:
    def __init__(self):
        self._actors = dict()
        self._msg_queue = deque()

    def new_actor(self, name, actor):
        self._msg_queue.append((actor, None))
        self._actors[name] = actor

    def send(self, name, msg):
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor, msg))

    def run(self):
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                actor.send(msg)
            except StopIteration:
                pass


def printer():
    while True:
        msg = yield
        print("Got:", msg)


def counter(sched):
    while True:
        n = yield
        if n == 0:
            break
        sched.send("printer", n)
        sched.send("counter", n-1)


if __name__ == "__main__":
    # sched = TaskScheduler()
    # sched.new_task(countdown(10))
    # sched.new_task(countdown(5))
    # sched.new_task(countup(15))
    # sched.run()

    # sched = ActorScheduler()
    # sched.new_actor('printer', printer())
    # sched.new_actor('counter', counter(sched))
    # sched.send('counter', 10000)
    # sched.run()

    p = printer()
    p.send(None)
    p.send(1)
