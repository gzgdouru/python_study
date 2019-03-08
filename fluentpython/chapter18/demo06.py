'''
每次下载发起多次请求
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


async def http_get(url):
    async with aiohttp.ClientSession() as session:
        res = await session.get(url)
        if res.status == 200:
            ctype = res.headers.get("Content-type", '').lower()
            if "json" in ctype or url.endswith("json"):
                data = await res.json()
            else:
                data = await res.read()
            return data
        elif res.status == 400:
            raise web.HTTPNotFound()
        else:
            res.raise_for_status()


async def get_country(cc):
    url = '{}/{}/metadata.json'.format(BASE_URL, cc.lower())
    metadata = await http_get(url)
    return metadata["country"]


async def get_flag(cc):
    url = "{}/{cc}/{cc}.gif".format(BASE_URL, cc=cc.lower())
    image = await http_get(url)
    return image


def show(text):
    print(text, end=" ")
    sys.stdout.flush()


async def download_one(cc, semaphore):
    try:
        async with semaphore:
            image = await get_flag(cc)

        async with semaphore:
            country = await get_country(cc)

    except web.HTTPNotFound:
        status = 404
        msg = "not found"
    except Exception as e:
        raise FetchError(cc) from e
    else:
        country = country.replace(" ", "_")
        filename = "{}-{}.gif".format(country, cc)
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, save_flag, image, filename)
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
