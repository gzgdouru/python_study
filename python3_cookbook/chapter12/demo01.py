'''
启动与停止线程
'''
import time
import threading


def countdown(n):
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(5)


class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)


if __name__ == "__main__":
    # t = threading.Thread(target=countdown, args=(10,))
    # t.start()

    # if t.is_alive():
    #     print("running.")
    # else:
    #     print("completed.")

    # t.join()

    c = CountdownTask()
    t = threading.Thread(target=c.run, args=(10,))
    t.start()
    c.terminate()
    t.join()
