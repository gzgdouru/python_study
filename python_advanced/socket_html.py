'''
使用sockte请求html数据
'''
import socket
from urllib.parse import urlparse

if __name__ == "__main__":
    url = r'http://blog.jobbole.com/all-posts/'

    # 从url中解析出主机和请求路径
    url = urlparse(url)
    host = url.netloc
    path = url.path if url.path else '/'
    print(host, path)

    #发送html请求
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, 80))
    http_request = "GET {path}\r\nHost:{host}\r\nConnection:close\r\n\r\n".format(path=path, host=host)
    sock.send(http_request.encode("utf-8"))

    #接收返回数据
    data = b""
    while True:
        d = sock.recv(1024)
        if d:
            data += d
        else:
            break
    print(data.decode("utf-8"))


