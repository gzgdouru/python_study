'''
理解事件驱动的IO
'''
import select
import socket
from datetime import datetime


class EventHandler:
    def fileno(self):
        raise NotImplemented('must implement')

    def wants_to_receive(self):
        return False

    def handle_receive(self):
        pass

    def wants_to_send(self):
        return False

    def handle_send(self):
        pass


def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.wants_to_receive()]
        wants_send = [h for h in handlers if h.wants_to_send()]
        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])

        for h in can_recv:
            h.handle_receive()

        for h in can_send:
            h.handle_send()


class UDPServer(EventHandler):
    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(address)

    def fileno(self):
        return self.sock.fileno()

    def wants_to_receive(self):
        return True


class UDPTimeServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(1)
        self.sock.sendto(datetime.now().strftime("%Y-%m-%d %H:%M:%S").encode("utf-8"), addr)


class UDPEchoServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(4096)
        self.sock.sendto(msg, addr)


class TCPServer(EventHandler):
    def __init__(self, address, client_handler, hander_list):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.sock.bind(address)
        self.sock.listen(1)
        self.client_hander = client_handler
        self.handler_list = hander_list

    def fileno(self):
        return self.sock.fileno()

    def wants_to_receive(self):
        return True

    def handle_receive(self):
        client, addr = self.sock.accept()
        self.handler_list.append(self.client_hander(client, self.handler_list))


class TCPHander(EventHandler):
    def __init__(self, sock, handler_list):
        self.sock = sock
        self.hander_list = handler_list
        self.outgoing = bytearray()

    def fileno(self):
        return self.sock.fileno()

    def close(self):
        self.sock.close()
        self.hander_list.remove(self)

    def wants_to_send(self):
        return True if self.outgoing else False

    def handle_send(self):
        nsent = self.sock.send(self.outgoing)
        self.outgoing = self.outgoing[nsent:]


class TCPEchoHandler(TCPHander):
    def wants_to_receive(self):
        return True

    def handle_receive(self):
        data = self.sock.recv(8192)
        if not data:
            self.close()
        else:
            self.outgoing.extend(data)


if __name__ == "__main__":
    handlers = []
    # handlers = [UDPTimeServer(('', 9000)), UDPEchoServer(('', 9001))]
    handlers.append(TCPServer(('', 9000), TCPEchoHandler, handlers))
    event_loop(handlers)
