'''
创建TCP服务器
'''
import time
from socketserver import BaseRequestHandler, TCPServer, StreamRequestHandler, ThreadingTCPServer
from concurrent.futures import ThreadPoolExecutor, as_completed
import socket


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        time.sleep(5)
        for msg in iter(lambda: self.request.recv(4096), b''):
            self.request.send(msg)


class EchoHandler2(StreamRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        for line in self.rfile:
            self.wfile.write(line)


if __name__ == "__main__":
    server = ThreadingTCPServer(('', 9000), EchoHandler2)
    server.serve_forever()

    # server = TCPServer(('', 9000), EchoHandler, bind_and_activate=False)
    # server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # server.server_bind()
    # server.server_activate()

    # TCPServer.allow_reuse_address = TCPServer
    # server = TCPServer(('', 9000), EchoHandler)
    # with ThreadPoolExecutor(max_workers=16) as executor:
    #     tasks = [executor.submit(server.serve_forever) for i in range(16)]
    #
    #     for task in as_completed(tasks):
    #         pass
