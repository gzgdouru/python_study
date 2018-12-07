'''
线程同步 - Semaphore的使用
Semaphore 是用于控制进入数量的锁
'''
from threading import Thread, Semaphore
import time


class UrlCustomer(Thread):
    def __init__(self, sem, url):
        super().__init__()
        self.sem = sem
        self.url = url

    def run(self):
        time.sleep(2)
        print("消耗url:{}".format(self.url))
        self.sem.release()


class UrlProducer(Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            url = "http://blog.jobbole.com/all-posts/{}.html".format(i)
            print("生产url:{}".format(url))
            self.sem.acquire()
            customer_thread = UrlCustomer(self.sem, url)
            customer_thread.start()


if __name__ == "__main__":
    sem = Semaphore(3)
    producer_thread = UrlProducer(sem)
    producer_thread.start()
