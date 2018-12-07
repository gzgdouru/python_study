
async def downloader(url):
    return "http://baidu.com"

async def get_url(url):
    html = await downloader(url)
    return html


if __name__ == "__main__":
    coro = get_url("http://baidu.com")
    coro.send(None)
