'''
简单的客户端认证
'''
import hmac
import os
from socket import socket, AF_INET, SOCK_STREAM

secret_key = b'peekaboo'


def client_authenticate(connection, secret_key):
    message = connection.recv(32)
    htext = hmac.new(secret_key, message)
    digest = htext.digest()
    connection.send(digest)


def server_authenticate(connection, secret_key):
    message = os.urandom(32)
    connection.send(message)
    htext = hmac.new(secret_key, message)
    digest = htext.digest()
    response = connection.recv(len(digest))
    return hmac.compare_digest(digest, response)


def echo_handler(client_sock):
    if not server_authenticate(client_sock, secret_key):
        client_sock.close()
        return

    while True:
        for msg in iter(lambda: client_sock.recv(4096), b''):
            client_sock.send(msg)


def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    while True:
        client_sock, client_addr = s.accept()
        echo_handler(client_sock)


if __name__ == "__main__":
    echo_server(('', 9000))
