import asyncio
import time

from tornado.web import RequestHandler, Application, URLSpec
from tornado import ioloop, httpclient


class MainHandler(RequestHandler):
    async def get(self, *args, **kwargs):
        http_client = httpclient.AsyncHTTPClient()
        response = await http_client.fetch("http://www.tornadoweb.org/en/stable/guide/structure.html")
        self.write(response.body)


class AsyncTestHandler(RequestHandler):
    async def get(self, id):
        await asyncio.sleep(5)
        # time.sleep(5)
        self.write("hello id:{0}".format(id))


if __name__ == "__main__":
    app = Application([
        URLSpec(r'/', MainHandler, name="index"),
        (r'/asynctest/(?P<id>\d+)', AsyncTestHandler),
    ])
    app.listen(8000)
    ioloop.IOLoop.current().start()
