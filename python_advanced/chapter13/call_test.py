import asyncio


def callback(sleep_times, loop):
    print("{0}, success time {1}".format(sleep_times, loop.time()))


def stop(loop):
    loop.stop()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    now = loop.time()
    # loop.call_at(now + 2, callback, 2, loop)
    loop.call_later(2, callback, 2, loop)
    loop.call_at(now + 1, callback, 1, loop)
    loop.call_at(now + 3, callback, 3, loop)
    loop.call_soon(callback, 4, loop)
    loop.call_at(now + 2, stop, loop)
    loop.run_forever()
