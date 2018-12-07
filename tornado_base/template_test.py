from tornado import web, ioloop


class MainHandler(web.RequestHandler):
    def get(self, *args):
        items = ["Item 1", "Item 2", "Item 3"]
        # self.write("hello world!")
        self.render("template.html", title="My title", items=items)

if __name__ == "__main__":
    app = web.Application([
        (r'/', MainHandler),
    ])
    app.listen(9000)
    ioloop.IOLoop.current().start()
