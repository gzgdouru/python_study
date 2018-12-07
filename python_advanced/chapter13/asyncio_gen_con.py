'''
asyncio实现生产者-消费者模式
'''
import asyncio
import random

queue = asyncio.Queue(maxsize=10)


async def gen_data():
    while True:
        await asyncio.sleep(1)
        data = random.randint(1, 1000)
        print("gen data: {0}".format(data))
        await queue.put(data)


async def con_data():
    while True:
        await asyncio.sleep(5)
        data = await queue.get()
        print("con data: {0}".format(data))


if __name__ == "__main__":
    tasks = [
        # asyncio.ensure_future(gen_data()),
        # asyncio.ensure_future(con_data()),
    ]
    loop = asyncio.get_event_loop()
    loop.create_task(gen_data())
    loop.create_task(con_data())
    loop.run_forever()
    # loop.run_until_complete(asyncio.gather(*tasks))
    # loop.close()
