'''
通过协程以动画形式显示文本式旋转指针
'''
import asyncio
import itertools


async def spin(msg):
    for char in itertools.cycle("|/-\\"):
        status = char + " " + msg
        print("\r{}".format(status), end="")
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break


async def slow_function():
    await asyncio.sleep(3)
    return 42


async def supervisor():
    spinner = asyncio.ensure_future(spin("thinking!"))
    print("spinner object:", spinner)
    result = await slow_function()
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print("\rAnswer:", result)


if __name__ == "__main__":
    main()
