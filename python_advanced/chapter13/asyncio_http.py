#asyncio 没有提供http协议的接口 aiohttp
import asyncio
import socket
from urllib.parse import urlparse

async def get_url(url):
    #通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    #建立socket连接
    reader, writer = await asyncio.open_connection(host,80)
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    all_lines = []
    async for raw_line in reader:
        data = raw_line.decode("utf8")
        all_lines.append(data)
    html = "\n".join(all_lines)
    return html


async def main():
    tasks = []
    for i in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(i)
        tasks.append(asyncio.ensure_future(get_url(url)))

    # futures, pendings = await asyncio.wait(tasks)
    # for future in futures:
    #     print(future.result())

    # results = await asyncio.gather(*tasks)
    # for result in results:
    #     print(result)

    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)
    # return await asyncio.gather(*tasks)

if __name__ == "__main__":
    import time
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # results = loop.run_until_complete(main())
    # for result in results:
    #     print(result)

    loop.close()