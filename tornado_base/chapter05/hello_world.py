from tornado import ioloop
from tornado.web import RequestHandler, Application


class MainHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello word!")

def make_app():
    return Application([
        (r'/', MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    ioloop.IOLoop.current().start()