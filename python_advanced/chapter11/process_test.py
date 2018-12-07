'''
多进程介绍
耗cpu的操作，用多进程编程， 对于io操作来说， 使用多线程编程，进程切换代价要高于线程
'''
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor
import time


# 1. 对于耗费cpu的操作，多进程由于多线程
def fib(n=10):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 2. 对于io操作来说，多线程优于多进程
def random_sleep(sleep_time):
    time.sleep(sleep_time)
    return sleep_time


if __name__ == "__main__":
    # 多线程耗时:42.46338748931885
    # with ThreadPoolExecutor(max_workers=3) as executor:
    # 多进程耗时:27.182592391967773
    # with ProcessPoolExecutor(max_workers=3) as executor:
    #     time_start = time.time()
    #     tasks = [executor.submit(fib, (i)) for i in range(25, 40)]
    #     for future in as_completed(tasks):
    #         print(future.result())
    #     print("耗时:{0}".format(time.time() - time_start))

    #多线程耗时:20.006199598312378
    #多进程耗时:20.294000148773193
    with ThreadPoolExecutor(max_workers=3) as executor:
        time_start = time.time()
        tasks = [executor.submit(random_sleep, (i)) for i in [2]*30]
        for future in as_completed(tasks):
            print(future.result())
        print("耗时:{0}".format(time.time() - time_start))
