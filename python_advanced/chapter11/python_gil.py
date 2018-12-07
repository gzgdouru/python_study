'''
python中的GIL介绍
python中一个线程对应于c语言中的一个线程
gil使得同一个时刻只有一个线程在一个cpu上执行字节码, 无法将多个线程映射到多个cpu上执行
gil会根据执行的字节码行数以及时间片释放gil，gil在遇到io的操作时候主动释放
'''

total = 0


def add():
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1


if __name__ == "__main__":
    import threading

    add_thread = threading.Thread(target=add)
    desc_thread = threading.Thread(target=desc)

    add_thread.start()
    desc_thread.start()

    add_thread.join()
    desc_thread.join()

    print(total)
