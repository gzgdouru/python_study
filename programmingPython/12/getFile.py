import sys, os, time, thread
from socket import *
import SocketServer

blkSize = 1024
defaultHost = "localhost"
defaultPort = 50007

helpText = '''
Usage...
server=> getFile.py -mode server
client=> getFile.py [-mode client] -file fff [-port nnn] [-host hhh]
'''

def now():
    return time.asctime()

def parsecommandline():
    dict = {}
    args = sys.argv[1:]
    while len(args) >= 2:
        dict[args[0]] = args[1]
        args = args[2:]
    return dict

def client(host, port, fileName):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send((fileName + "\n"))
    dropDir = os.path.split(fileName)[1]
    file = open(dropDir, "wb")
    while True:
        data = sock.recv(blkSize)
        if not data: break
        file.write(data)
    sock.close()
    file.close()
    print "client got", fileName, "at", now()

def serverThread(clientSock):
    sockFile = clientSock.makefile("r")
    fileName = sockFile.readline()[:-1]
    try:
        file = open(fileName, "rb")
        while True:
            bytes = file.read(blkSize)
            if not bytes: break
            sent = clientSock.send(bytes)
            assert sent == len(bytes)
    except:
        print "error download file on server:", fileName
    clientSock.close()

def server(host, port):
    serverSock = socket(AF_INET, SOCK_STREAM)
    serverSock.bind((host, port))
    serverSock.listen(5)
    while True:
        clientSock, clientAddr = serverSock.accept()
        print "server connect by", clientAddr, "at", now()
        thread.start_new_thread(serverThread, (clientSock,))

class FileLoadServer(SocketServer.BaseRequestHandler):
    def handle(self):
        print "server connect by", self.client_address, "at", now()
        serverThread(self.request)

def main(args):
    host = args.get("-host", defaultHost)
    port = args.get("-port", defaultPort)
    if args.get("-mode") == "server":
        if host == "localhost": host = ""
        #server(host, port)
        tmpServer = SocketServer.ThreadingTCPServer((host, port), FileLoadServer)
        tmpServer.serve_forever()
    elif args.get("-file"):
        client(host, port, args["-file"])
    else:
        print helpText

if __name__ == "__main__":
    args = parsecommandline()
    main(args)