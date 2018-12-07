'''
协程同步
'''
import asyncio
import time
import aiohttp

total = 0


async def add():
    global total
    for i in range(1000000):
        total += 1


async def desc():
    global total
    for i in range(1000000):
        total -= 1


lock = asyncio.Lock()
cache = {}


async def get_url(url):
    async with lock:
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request("GET", url)
        cache[url] = stuff
        return stuff


async def parse_stuff(url):
    stuff = await get_url(url)
    print("parse_stuff: {0}".format(stuff))


async def use_stuff(url):
    stuff = await get_url(url)
    print("use_stuff: {0}".format(stuff))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # task_add = add()
    # task_desc = desc()
    # loop.run_until_complete(asyncio.gather(*(task_add, task_desc)))
    # loop.close()
    # print(total)

    tasks = [parse_stuff("http://shop.projectsedu.com/goods/1/"), use_stuff("http://shop.projectsedu.com/goods/1/")]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()