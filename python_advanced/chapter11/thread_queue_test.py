'''
线程间通信-queue的使用
'''
from queue import Queue, Empty
import threading
import time
from urllib import parse

class GetDetailUrl(threading.Thread):
    def __init__(self, name, url, queue):
        super().__init__(name=name)
        self.url = url
        self.queue = queue

    def run(self):
        #假设每2秒产生一个detail_url
        print("{0}线程启动!".format(self.name))
        time_start = time.time()
        for i in range(5):
            time.sleep(2)
            url = parse.urljoin(self.url, "{0}.html".format(i))
            print("线程{0}产生url:{1}".format(self.name, url))
            self.queue.put(url)
        print("{0}线程结束, 耗时:{1}".format(self.name, time.time()-time_start))


class GetDetaiHtml(threading.Thread):
    def __init__(self, name, queue):
        super().__init__(name=name)
        self.queue = queue

    def run(self):
        #假设每4秒消耗一个detail_url
        print("{0}线程启动!".format(self.name))
        while True:
            try:
                url = self.queue.get_nowait()
                time.sleep(4)
                queue.task_done()
                print("线程{0}消耗url:{1}".format(self.name, url))
            except Empty as e:
                time.sleep(0.2)


if __name__ == "__main__":
    url = "http://blog.jobbole.com/all-posts/"
    queue = Queue(maxsize=1000)
    gen_thread = GetDetailUrl("gen_thread", url, queue)
    gen_thread.setDaemon(True)
    gen_thread.start()

    con_threads = []
    for i in range(10):
        con_thread = GetDetaiHtml("con_thread_{0}".format(i), queue)
        con_thread.setDaemon(True)
        con_thread.start()
        con_threads.append(con_thread)

    gen_thread.join()
    # [con_thread.join() for con_thread in con_threads]
    queue.join()