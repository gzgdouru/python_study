from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from xmlrpc.client import ServerProxy
import hmac


def client_authenticate(connection, secret_key):
    message = connection.recv(32)
    htext = hmac.new(secret_key, message)
    digest = htext.digest()
    connection.send(digest)


if __name__ == "__main__":
    # s = ServerProxy('http://localhost:9000', allow_none=True)
    # s.set("foo", "bar")
    # print(s.get("foo"))
    #
    # s.set('spam', [1, 2, 3])
    # print(s.keys())

    # secret_key = b'peekaboo11'
    # s = socket(AF_INET, SOCK_STREAM)
    # s.connect(("localhost", 9000))
    # client_authenticate(s, secret_key)
    # s.send(b'hello world!')
    # resp = s.recv(4096)
    # print(resp)

    # s = socket(AF_INET, SOCK_DGRAM)
    # s.sendto(b'hahah', ("localhost", 9001))
    # msg = s.recvfrom(4096)
    # print(msg)

    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("localhost", 9000))
    s.send(b"hello")
    msg = s.recv(4096)
    print(msg)