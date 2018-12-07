from tornado import web, ioloop


class MainHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello word!")


class PeopleIdHandler(web.RequestHandler):
    def initialize(self, name):
        self.name = name

    def get(self, id, *args, **kwargs):
        # self.write("用户id:{}".format(id))
        self.redirect(self.reverse_url("people_name", "bobby"))


class PeopleNameHandler(web.RequestHandler):
    def get(self, name, *args, **kwargs):
        self.write("用户姓名:{}".format(name))

class PeopleInfoHanler(web.RequestHandler):
    def get(self, name, age, gender, *args, **kwargs):
        self.write("用户姓名:{}, 用户年龄:{}, 用户性别:{}".format(name, age, gender))


urls = [
    web.URLSpec(r'/', MainHandler, name="index"),
    web.URLSpec(r'/people/(?P<id>\d+)/?', PeopleIdHandler, {"name": "wanlaji"}, name="people_id"),
    web.URLSpec(r'/people/(?P<name>\w+)/?', PeopleNameHandler, name="people_name"),
    web.URLSpec(r'/people/(\w+)/(\d+)/(\w+)/?', PeopleInfoHanler, name="people_info"),
]

if __name__ == "__main__":
    app = web.Application(urls, debug=True)
    app.listen(8888)
    ioloop.IOLoop.current().start()
