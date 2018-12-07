'''
线程同步-condition(条件变量)的使用
'''
from threading import Thread, Condition
import time


class TianMao(Thread):
    def __init__(self, name, cond):
        super().__init__(name=name)
        self.cond = cond

    def run(self):
        with self.cond:
            print("{} : 小爱同学 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 我们来对古诗吧 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 我住长江头 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 日日思君不见君 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 此水几时休 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 只愿君心似我心 ".format(self.name))
            self.cond.notify()
            self.cond.wait()


class XiaoAi(Thread):
    def __init__(self, name, cond):
        super().__init__(name=name)
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{} : 在 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 好啊 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 君住长江尾 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 共饮长江水 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 此恨何时已 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 定不负相思意 ".format(self.name))
            self.cond.notify()


urls = []


class GenUrl(Thread):
    def __init__(self, name, cond):
        super().__init__(name=name)
        self.cond = cond

    def run(self):
        global urls
        for i in range(1, 6):
            url = "http://blog.jobbole.com/all-posts/{0}.html".format(i)
            time.sleep(2)
            with self.cond:
                urls.append(url)
                print("生产 url:{0}".format(url))
                self.cond.notify()


class ConUrl(Thread):
    def __init__(self, name, cond):
        super().__init__(name=name)
        self.cond = cond

    def run(self):
        global urls
        while True:
            with self.cond:
                self.cond.wait()
                url = urls.pop()
                print("线程{0}消费 url:{1}".format(self.name, url))


if __name__ == "__main__":
    cond = Condition()

    # tiaomao_thread = TianMao(name="天猫", cond=cond)
    # xiaoai_thread = XiaoAi(name="小爱", cond=cond)
    #
    # xiaoai_thread.start()
    # tiaomao_thread.start()
    #
    # xiaoai_thread.join()
    # tiaomao_thread.join()

    gen_thread = GenUrl("gen_url_thread", cond)

    con_threads = []
    for i in range(1, 11):
        con_thread = ConUrl("con_url_thread_{0}".format(i), cond)
        con_thread.start()
        con_threads.append(con_thread)
    gen_thread.start()