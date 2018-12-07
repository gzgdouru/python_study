from tornado import web, ioloop


class RedirectTestHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect("https://ljwancaiji.com")


if __name__ == "__main__":
    app = web.Application([
        (r'/', RedirectTestHandler),
        (r'/guess', web.RedirectHandler, dict(url="http://guessdice.ljwancaiji.com"))
    ])
    app.listen(8000)
    ioloop.IOLoop.current().start()
