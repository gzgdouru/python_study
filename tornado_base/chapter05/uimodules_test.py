import os

from tornado import web, ioloop


class OrderModule(web.UIModule):
    def cal_total(self, price, nums):
        return price * nums

    def render(self, order, *args, **kwargs):
        return self.render_string("ui_modules/order-list.html", order=order, cal_total=self.cal_total)


class MainHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        orders = [
            {
                "name": "小米T恤 忍者米兔双截棍 军绿 XXL",
                "image": "http://i1.mifile.cn/a1/T11lLgB5YT1RXrhCrK!40x40.jpg",
                "price": 39,
                "nums": 3,
                "detail": "<a href='http://www.baidu.com'>查看详情</a>"
            },
            {
                "name": "招财猫米兔 白色",
                "image": "http://i1.mifile.cn/a1/T14BLvBKJT1RXrhCrK!40x40.jpg",
                "price": 49,
                "nums": 2,
                "detail": "<a href='http://www.baidu.com'>查看详情</a>"
            },
            {
                "name": "小米圆领纯色T恤 男款 红色 XXL",
                "image": "http://i1.mifile.cn/a1/T1rrDgB4DT1RXrhCrK!40x40.jpg",
                "price": 59,
                "nums": 1,
                "detail": "<a href='http://www.baidu.com'>查看详情</a>"
            }
        ]

        self.render("index2.html", orders=orders)


settings = {
    "static_path": os.path.join(os.path.abspath(os.path.dirname(__file__)), "static"),
    "static_url_prefix": "/static/",
    "template_path": "templates",
    "ui_modules": {
        "OrderModule": OrderModule,
    },

}

if __name__ == "__main__":
    app = web.Application([
        web.URLSpec(r'/', MainHandler, name="index"),
    ], debug=True, **settings)
    app.listen(8888)
    ioloop.IOLoop.current().start()
