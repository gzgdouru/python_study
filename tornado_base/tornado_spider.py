from urllib import parse

from tornado import httpclient, ioloop, queues, gen
from scrapy.selector import Selector

base_url = "http://www.tornadoweb.org/en/stable/"
concurrency = 3


async def parse_links(url):
    # await gen.sleep(1)
    response = await httpclient.AsyncHTTPClient().fetch(url)
    print(f"fetched {url}")

    html = response.body.decode("utf-8")
    return get_links(html)


def get_links(html):
    selector = Selector(text=html)
    urls = selector.css("a::attr(href)").extract()
    urls = [parse.urljoin(base_url, remove_fragment(url)) for url in urls]
    return urls


def remove_fragment(url):
    pure_url, frag = parse.urldefrag(url)
    return pure_url


async def main():
    queue = queues.Queue()
    fetching, fetched = set(), set()

    async def fetch_url(current_url):
        if current_url in fetching:
            return
        print(f"fetching {current_url}")
        fetching.add(current_url)
        urls = await parse_links(current_url)
        fetched.add(current_url)

        for new_url in urls:
            if new_url.startswith(base_url):
                await queue.put(new_url)

    async def worker():
        async for url in queue:
            if url is None:
                return
            try:
                await fetch_url(url)
            except Exception as e:
                print(f"Exception {e}:{url}")
            finally:
                queue.task_done()

    await queue.put(base_url)
    workers = gen.multi(worker() for _ in range(concurrency))
    await queue.join()
    print("Done!")

    for _ in range(concurrency):
        await queue.put(None)

    await workers


if __name__ == "__main__":
    loop = ioloop.IOLoop.current()
    loop.run_sync(main)
