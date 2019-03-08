import socket

if __name__ == "__main__":
    address = "127.0.0.1"
    port = 2323

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((address, port))

    # data = sock.recv(4096)
    # print(data.decode())

    data = input(">")
    sock.send(data.encode())

    while True:
        data = sock.recv(4096)
        if not data:
            break
        print(data)
