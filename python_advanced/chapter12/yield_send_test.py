'''
yield中send函数使用
'''


def get_html():
    # html = yield
    yield 1
    return "test complate!"


if __name__ == "__main__":
    gen = get_html()
    # 在调用send发送非none值之前，我们必须启动一次生成器， 方式有两种1. gen.send(None), 2. next(gen)
    print(gen.send(None))

    # send方法可以传递值进入生成器内部，同时还可以重启生成器执行到下一个yield位置
    gen.send("oa.anjubao.cn")
