'''
RequestHandler的子类
'''
import os

from tornado import web, ioloop


class MainHandler(web.RequestHandler):
    # 当客户端发起不同的http方法的时候， 只需要重载handler中的对应的方法即可
    async def get(self, *args, **kwargs):
        self.write("hello world")


settings = {
    "static_path": os.path.join(os.path.abspath(os.path.dirname(__file__)), "static"),
    "static_url_prefix": "/static/",
}

if __name__ == "__main__":
    app = web.Application([
        ("/", MainHandler),
        ("/(\d+)/", web.RedirectHandler, {"url": "/"}),
        # ("/static/(.*)", web.StaticFileHandler, {"path": os.path.join(os.path.abspath(os.path.dirname(__file__)), "static")}),
    ], debug=True, **settings)
    app.listen(8888)
    ioloop.IOLoop.current().start()
