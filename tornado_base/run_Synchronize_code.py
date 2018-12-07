'''
tornado运行同步的代码
'''
import time
import asyncio

from tornado import ioloop
from tornado.gen import multi

from http_client_test import fetch, async_fetch

def get_html(url):
    time.sleep(2)
    print("url:{0}".format(url))


if __name__ == "__main__":
    start_time = time.time()
    loop = ioloop.IOLoop.current()
    loop.run_in_executor(None, get_html, "http://www.baidu.com")
    loop.run_in_executor(None, get_html, "http://jobbole.com")
    print(time.time()-start_time)
