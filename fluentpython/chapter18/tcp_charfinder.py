import sys
import asyncio

from charfinder import UnicodeNameIndex

CRLF = b"\r\n"
PROMPT = b"?>"
index = UnicodeNameIndex()


async def handle_queries(reader, writer):
    while True:
        # writer.write(PROMPT)
        # await writer.drain()
        data = await reader.read(4096)
        print(data)
        try:
            query = data.decode().strip()
        except UnicodeDecodeError:
            query = "\x00"
        client = writer.get_extra_info("peername")
        print("Received from {}: {}".format(client, query))
        if query:
            if ord(query[:1]) < 32:
                break
            lines = list(index.find_description_strs(query))
            if lines:
                writer.writelines(line.encode() + CRLF for line in lines)
            writer.write(index.status(query, len(lines)).encode() + CRLF)
            await writer.drain()
            print("Sent {} results".format(len(lines)))

    print("Close the client socket")
    writer.close()


def main():
    address = "127.0.0.1"
    port = 2323
    loop = asyncio.get_event_loop()
    server = loop.run_until_complete(asyncio.start_server(handle_queries, address, port))
    host = server.sockets[0].getsockname()
    print("Serving on {}. Hit CTRL-C to stop.".format(host))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    print("Server shutting down.")
    server.close()

    loop.run_until_complete(server.wait_closed())
    loop.close()

if __name__ == "__main__":
    main()
