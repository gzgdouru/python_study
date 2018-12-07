from tornado import web
from tornado import ioloop


class MainHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('<a href="%s">link to story 1</a>' %
                   self.reverse_url("story", "1"))


class StoryHandler(web.RequestHandler):
    def initialize(self, db):
        self.db = db

    def get(self, story_id):
        self.write("this is story %s" % story_id)


if __name__ == "__main__":
    app = web.Application([
        web.URLSpec(r'/', MainHandler),
        web.URLSpec(r'/story/(?P<story_id>\d+)', StoryHandler, dict(db="mysql"), name="story")
    ])
    app.listen(8000)
    ioloop.IOLoop.current().start()