'''
RequestHanler的一些常用方法
'''
import json

from tornado import web, ioloop


class MainHandler(web.RequestHandler):
    #入口方法
    def initialize(self):
        #用于初始化handler类的过程
        pass

    def prepare(self):
        #prepare方法用于真正调用请求处理之前的初始化方法
        #1. 打印日志， 打开文件
        pass

    def on_finish(self):
        #请求结束时调用的清理方法
        #关闭句柄， 清理内存
        pass

    # http方法
    def get(self, *args, **kwargs):
        #从请求的query string返回给定name的参数的值
        # data1 = self.get_query_argument("name")
        # data2 = self.get_query_arguments("name")

        #返回指定的name参数的值.
        data1 = self.get_argument("name")
        data2 = self.get_arguments("name")
        print(data1, data2)
        pass

    def post(self, *args, **kwargs):
        # 返回指定的name参数的值.
        # data1 = self.get_argument("name")
        # data2 = self.get_arguments("name")

        #返回请求体中指定name的参数的值.
        # data1 = self.get_body_argument("name")
        # data2 = self.get_body_arguments("name")

        #处理json提交的数据
        param = self.request.body.decode("utf-8")
        json.loads(param)

        self.finish(param)

    def delete(self, *args, **kwargs):
        pass
    def put(self, *args, **kwargs):
        pass
    def patch(self, *args, **kwargs):
        pass

    #输出方法
    # def set_status(self, status_code, reason=None):
    #     pass
    # def write(self, chunk):
    #     pass
    # def finish(self, chunk=None):
    #     pass
    # def redirect(self, url, permanent=False, status=None):
    #     pass
    # def write_error(self, status_code, **kwargs):
    #     pass


if __name__ == "__main__":
    app = web.Application([
        (r'/', MainHandler),
    ], debug=True)
    app.listen(8888)
    ioloop.IOLoop.current().start()
