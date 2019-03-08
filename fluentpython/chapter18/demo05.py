'''
完整版协程版下载国旗
'''
import os
import sys
import time
import asyncio
from collections import namedtuple, Counter

import aiohttp
from aiohttp import web
import tqdm

Result = namedtuple("Result", "status country")

POP20_CC = "CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR".split()
BASE_URL = r'http://flupy.org/data/flags'
BASE_DIR = "downloads/"
DEFAULT_CONCUR_REQ = 6
MAX_CONCUR_REQ = 1000


class FetchError(Exception):
    def __init__(self, country_code):
        self.country_code = country_code


def save_flag(img, filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "wb") as f:
        f.write(img)


async def get_flag(cc):
    url = "{}/{cc}/{cc}.gif".format(BASE_URL, cc=cc.lower())
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url)
        if resp.status == 200:
            image = await resp.read()
            return image
        elif resp.status == 404:
            raise web.HTTPNotFound()
        else:
            raise resp.raise_for_status()


def show(text):
    print(text, end=" ")
    sys.stdout.flush()


async def download_one(cc, semaphore):
    try:
        async with semaphore:
            image = await get_flag(cc)
    except web.HTTPNotFound:
        status = 404
        msg = "not found"
    except Exception as e:
        raise FetchError(cc) from e
    else:
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, save_flag, image, f"{cc}.jpg")
        status = 200
        msg = "ok"

    if msg:
        print(cc, msg)

    return Result(status, msg)


async def downloader_coro():
    counter = Counter()
    semaphore = asyncio.Semaphore(DEFAULT_CONCUR_REQ)
    to_do = [download_one(cc, semaphore) for cc in POP20_CC]

    to_do_iter = asyncio.as_completed(to_do)
    to_do_iter = tqdm.tqdm(to_do_iter, total=len(POP20_CC))
    for future in to_do_iter:
        try:
            res = await future
        except FetchError as e:
            country_code = e.country_code
            try:
                error_msg = e.__cause__.args[0]
            except IndexError:
                error_msg = e.__cause__.__class__.__name__

            if error_msg:
                print("*** Error for {}:{}".format(country_code, error_msg))

            status = 500
        else:
            status = res.status

        counter[status] += 1
    return counter


def download_many():
    loop = asyncio.get_event_loop()
    coro = downloader_coro()
    counts = loop.run_until_complete(coro)
    loop.close()
    return counts


def main(download_many):
    t0 = time.time()
    count = download_many()
    elapsed = time.time() - t0
    print("\n{} flags download in {:.2f}s".format(count, elapsed))


if __name__ == "__main__":
    main(download_many)
