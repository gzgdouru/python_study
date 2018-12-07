'''
线程同步-Lock、RLock(可重入锁)的使用
在同一个线程里面，可以连续调用多次acquire， 一定要注意acquire的次数要和release的次数相等
1. 用锁会影响性能
2. 锁会引起死锁
死锁的情况 A（a，b）
A(a、b)
acquire (a)
acquire (b)

B(a、b)
acquire (a)
acquire (b)
'''
import threading

total = 0
# lock = threading.Lock()
lock = threading.RLock()


def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        lock.acquire()
        total += 1
        lock.release()
        lock.release()


def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


if __name__ == "__main__":
    add_thread = threading.Thread(target=add)
    desc_thread = threading.Thread(target=desc)

    add_thread.start()
    desc_thread.start()

    add_thread.join()
    desc_thread.join()

    print(total)
