'''
事件循环+回调（驱动生成器）+epoll(IO多路复用)
asyncio是python用于解决异步io编程的一整套解决方案
'''
import asyncio
import time
from functools import partial


async def get_html(url):
    print("start get html!")
    await asyncio.sleep(2)
    print("end get html!")


async def get_html_1(url):
    print("get url:{0} start".format(url))
    await asyncio.sleep(2)
    print("get url:{0} end".format(url))
    return "bobby"


def callback(url, future):
    print(url, future.result())


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()

    future = asyncio.ensure_future(get_html("www.baidu.com"))
    loop.run_until_complete(future)
    print(time.time() - start_time)
    loop.close()

    # tasks = [get_html("www.baidu.com") for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))
    # print(time.time()-start_time)
    # loop.close()

    # task = loop.create_task(get_html_1("www.baidu.com"))
    # task.add_done_callback(partial(callback, "ljwancaiji.com"))
    # loop.run_until_complete(task)
    #print(time.time()-start_time)
    # loop.close()

    #gather
    # tasks = [get_html_1("http://ljwancaiji.com/{0}.html".format(i)) for i in range(10)]
    # loop.run_until_complete(asyncio.gather(*tasks))
    # loop.close()
    # print(time.time() - start_time)

    # gather和wait的区别
    # group1 = [get_html_1("http://ljwancaiji.com/{0}.html".format(i)) for i in range(2)]
    # group2 = [get_html_1("http://imooc.com/{0}.html".format(i)) for i in range(2)]
    # group1 = asyncio.gather(*group1)
    # group2 = asyncio.gather(*group2)
    # group2.cancel()
    # loop.run_until_complete(asyncio.gather(group1, group2))
    # loop.close()
    # print(time.time() - start_time)