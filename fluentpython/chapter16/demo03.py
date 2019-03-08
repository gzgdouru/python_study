'''
终于协程和异常处理
'''
import inspect


class DemoException(Exception):
    pass


def demo_exc_handling():
    print("-> coroutine started")
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print("*** DemoException handled. Continuing...")
            else:
                print("-> coroutine received: {}".format(x))
    finally:
        print("-> coroutine end")


if __name__ == "__main__":
    exc_coro = demo_exc_handling()
    exc_coro.send(None)
    exc_coro.send(11)
    exc_coro.send("hello world")
    exc_coro.throw(DemoException("hhha"))
    # exc_coro.close()
    print(inspect.getgeneratorstate(exc_coro))
