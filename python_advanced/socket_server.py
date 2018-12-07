import socket
import threading


def handle_sock(client_sock, client_addr):
    while True:
        data = client_sock.recv(1024)
        if not data:
            print("{0} 已退出!".format(client_addr))
            break
        print("{0}:{1}".format(client_addr, data.decode("utf-8")))
        data = input("{0}>".format(client_addr))
        client_sock.send(data.encode("utf-8"))
    client_sock.close()


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", 8000))
    sock.listen(10)

    while True:
        client_sock, client_addr = sock.accept()
        thread = threading.Thread(target=handle_sock, args=(client_sock, client_addr))
        thread.start()
