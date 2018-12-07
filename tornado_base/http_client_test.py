from tornado.httpclient import HTTPClient, AsyncHTTPClient
from tornado import ioloop


# 同步的http client
def fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    print(response.body.decode("utf-8"))


# 异步的http client
async def async_fetch(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body.decode("utf-8")


if __name__ == "__main__":
    # fetch("http://shop.projectsedu.com/goods/1/")
    loop = ioloop.IOLoop.current()
    loop.run_sync(lambda: async_fetch("http://shop.projectsedu.com/goods/1/"))

