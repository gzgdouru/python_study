import SocketServer, time

myHost = ""
myPort = 50007

def now():
    return time.ctime()

class MyClientHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print self.client_address, now()
        time.sleep(5)
        while True:
            data = self.request.recv(1024)
            if not data: break
            reply = "Echo=>%s at %s" % (data, now())
            self.request.send(reply)
        self.request.close()

myAddr = (myHost, myPort)
server = SocketServer.ThreadingTCPServer(myAddr, MyClientHandler)
server.serve_forever()