'''
试验Executor.map方法
'''
import time
from concurrent import futures


def display(*args):
    print(time.strftime("[%H:%M:%S]"), end=" ")
    print(*args)


def loiter(n):
    display("{}loiter({}): doing nothing for {}s".format("\t" * n, n, n))
    time.sleep(n)
    display("{}loter({}): done.".format("\t" * n, n))
    return n * 10

def main():
    display("Script starting.")
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(6, 1, -1))
    display("results:", results)
    display("Waiting for individual results:")
    for i, result in enumerate(results):
        display("result:{}: {}".format(i, result))

if __name__ == "__main__":
    main()
