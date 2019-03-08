'''
协程版下载国旗
'''
import os
import sys
import time
import asyncio

import aiohttp

POP20_CC = "CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR".split()
BASE_URL = r'http://flupy.org/data/flags'
BASE_DIR = "downloads/"


def save_flag(img, filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "wb") as f:
        f.write(img)


async def get_flag(cc):
    url = "{}/{cc}/{cc}.gif".format(BASE_URL, cc=cc.lower())
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url)
        image = await resp.read()
    return image


def show(text):
    print(text, end=" ")
    sys.stdout.flush()

async def download_one(cc):
    image = await get_flag(cc)
    show(cc)
    save_flag(image, f"{cc}.gif")
    return cc


def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in cc_list]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    print("\n{} flags download in {:.2f}s".format(count, elapsed))


if __name__ == "__main__":
    main(download_many)
