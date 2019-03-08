'''
通过线程以动画形式显示文本式旋转指针
'''
import threading
import itertools
import time
import sys


class Signal:
    go = True


def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle("|/-\\"):
        status = char + " " + msg
        print("\r{}".format(status), end="")
        time.sleep(0.1)
        if not signal.go:
            break


def slow_function():
    time.sleep(3)
    return 42


def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=("thinking!", signal))
    print("spinner object:", spinner)
    spinner.start()
    result = slow_function()
    signal.go = False
    spinner.join()
    return result


def main():
    result = supervisor()
    print("\rAnswer:", result)


if __name__ == "__main__":
    main()
