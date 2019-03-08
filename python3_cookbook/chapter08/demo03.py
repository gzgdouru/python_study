'''
让对象支持上下文管理协议
'''
import socket
from functools import partial


class LazyConnection:
    def __init__(self, address, family=socket.AF_INET, sock_type=socket.SOCK_STREAM):
        self.address = address
        self.family = family
        self.sock_type = sock_type
        self.sock = None

    def __enter__(self):
        sock = socket.socket(self.family, self.sock_type)
        sock.connect(self.address)
        self.sock = sock
        return sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.sock:
            self.sock.close()


if __name__ == "__main__":
    with LazyConnection(('www.python.org', 80)) as conn:
        text = "GET /index.html HTTP/1.0\r\nHost: www.python.org\r\n\r\n"
        conn.send(text.encode("utf-8"))
        for data in iter(partial(conn.recv, 8192), b''):
            print(data.decode("utf-8"))
