'''
创建UDP服务器
'''
from socketserver import BaseRequestHandler, UDPServer
from datetime import datetime


class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        msg, sock = self.request
        resp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sock.sendto(resp.encode("utf-8"), self.client_address)

if __name__ == "__main__":
    server = UDPServer(('', 9000), TimeHandler)
    server.serve_forever()
