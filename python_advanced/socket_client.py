import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 8000))
while True:
    data = input(">")
    sock.send(data.encode("utf-8"))
    data = sock.recv(1024)
    print(data.decode("utf-8"))