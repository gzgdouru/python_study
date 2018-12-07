from tornado.web import RequestHandler, Application, URLSpec
from tornado import ioloop


class MyFormHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('<html><body><form action="/" method="POST">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self, *args, **kwargs):
        self.set_header("Content-Type", "text/plain")
        msg = self.get_body_argument("message")
        self.write("You wrote {0}".format(msg))


if __name__ == "__main__":
    app = Application([
        URLSpec(r'/', MyFormHandler, name="index"),
    ])
    app.listen(8000)
    ioloop.IOLoop.current().start()
