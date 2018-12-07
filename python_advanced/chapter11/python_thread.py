'''
python多线程的使用
对于io操作来说，多线程和多进程性能差别不大
'''
import threading
import time


def get_detail_url(url):
    print("get detail url started")
    time.sleep(2)
    print("get detail url end")


def get_detail_html(url):
    print("get detail html started")
    time.sleep(4)
    print("get detail html end")


class GetDetailUrl(threading.Thread):
    def __init__(self, url, name):
        self.url = url
        super().__init__(name=name)

    def run(self):
        print("{0} start".format(self.name))
        time_start = time.time()
        time.sleep(2)
        print("{0} end, 耗时:{1}".format(self.name, time.time() - time_start))


class GetDetailHtml(threading.Thread):
    def __init__(self, url, name):
        self.url = url
        super().__init__(name=name)

    def run(self):
        print("{0} start".format(self.name))
        time_start = time.time()
        time.sleep(4)
        print("{0} end, 耗时:{1}".format(self.name, time.time() - time_start))


if __name__ == "__main__":
    url = r'http://blog.jobbole.com/all-posts/'
    # thread1 = threading.Thread(target=get_detail_url, args=(url,))
    # thread2 = threading.Thread(target=get_detail_html, args=(url,))
    #
    # thread1.start()
    # thread2.start()
    #
    # time_start = time.time()
    # thread1.join()
    # thread2.join()
    # print("last time:{0}".format(time.time() - time_start))

    thread1 = GetDetailUrl(url, "get_detail_url")
    thread2 = GetDetailHtml(url, "get_detail_html")
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
