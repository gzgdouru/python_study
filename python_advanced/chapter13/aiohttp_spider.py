import asyncio
from urllib import parse
import re
from datetime import datetime

import aiohttp
import aiomysql
from scrapy.selector import Selector

start_url = "http://blog.jobbole.com/"
seen_urls = set()
queue = asyncio.Queue()
sem = asyncio.Semaphore(3)


async def get_html(session, url):
    async with sem:
        try:
            async with session.get(url) as resp:
                seen_urls.add(url)
                html = await resp.text()
                return html
        except Exception as e:
            print(e)

async def parse_urls(session, url):
    html = await get_html(session, url)
    selector = Selector(text=html)
    urls = selector.xpath("//a/@href").extract()
    match_pattern = re.compile(r'^http://blog.jobbole.com/\d+/$')
    for url in urls:
        url = parse.urljoin(start_url, url)
        if url not in seen_urls:
            await queue.put(url)


async def parse_detail(pool):
    async with aiohttp.ClientSession() as session:
        while True:
            url = await queue.get()
            if url not in seen_urls:
                match_obj = re.match(r'http://blog.jobbole.com/(\d+)/$', url)
                if match_obj:
                    html = await get_html(session, url)
                    selector = Selector(text=html)
                    id = int(match_obj.group(1))
                    title = selector.css(".entry-header h1::text").extract_first()
                    async with pool.acquire() as conn:
                        async with conn.cursor() as cur:
                            sql = '''
                            insert into tb_jobbole(id, title, add_time) 
                            values({id}, '{title}', '{add_time}')
                            on duplicate key update add_time = '{add_time}'
                            '''.format(id=id, title=title, add_time=datetime.now())
                            await cur.execute(sql)
                            # print(sql)
                else:
                    await parse_urls(session, url)
            else:
                print("过滤重复的url:{0}".format(url))


async def main(loop):
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='123456',
                                      db='mytest', loop=loop,
                                      charset="utf8", autocommit=True)
    async with aiohttp.ClientSession() as session:
        await parse_urls(session, start_url)
        asyncio.ensure_future(parse_detail(pool))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(main(loop))
    loop.run_forever()
