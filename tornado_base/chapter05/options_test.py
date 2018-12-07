from tornado import web, options, ioloop

# define， 定义一些可以在命令行中传递的参数以及类型
options.define("port", default=8888, help="run on the given port", type=int)
options.define("debug", default=True, help="set tornado debug mode", type=bool)

# options是一个类，全局只有一个options
# options.options.parse_command_line()
options.options.parse_config_file("conf.cfg")


class MainHandler(web.RequestHandler):
    async def get(self, *args, **kwargs):
        self.write("hello world")


if __name__ == "__main__":
    app = web.Application([
        (r'/', MainHandler)
    ], debug=options.options.debug)
    # print(options.options.debug)
    app.listen(options.options.port)
    ioloop.IOLoop.current().start()
