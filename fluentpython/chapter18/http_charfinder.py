import asyncio
from aiohttp import web

from charfinder import UnicodeNameIndex

index = UnicodeNameIndex()


def home(request):
    query = request.GET.get("query", "").strip()
    print("Query: {}".format(query))
    if query:
        descriptions = list(index.find_description_strs(query))
        res = "\n".join(ROW_TPL.format(**vars(desc)) for desc in descriptions)
        msg = index.status(query, len(descriptions))
    else
        descriptions = []
        res = ""
        msg = "Enter words describing characters."
    html = template.format(query, res, msg)
    print("Sending {} results.".format(len(descriptions)))
    return web.Response(content_type=CONTENT_TYPE, text=html)


async def init(loop, address, port):
    app = web.Application(loop=loop)
    app.router.add_route("GET", "/", home)
    handler = app.make_handler()
    server = await loop.create_server(handler, address, port)
    return server.sockets[0].getsockname()


def main():
    address = "127.0.0.1"
    port = 8888
    loop = asyncio.get_event_loop()
    host = loop.run_until_complete(init(loop, address, port))
    print("Serving on {}. Hit CTRL-C to stop.".format(host))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    print("Server shutting down.")
    loop.close()


if __name__ == "__main__":
    main()
