import sys
from socket import *
import threading

#serverHost = "192.168.232.130"
serverHost = "localhost"
serverPort = 50007
message = ["hello network world"]
lock = threading.Lock()

def run(i):
    sockObj = socket(AF_INET, SOCK_STREAM)
    sockObj.connect((serverHost, serverPort))
    for line in message:
        sockObj.send(line)
        data = sockObj.recv(1024)
        with lock:
            print "threadId:%d client recv:%s" % (i, data)
    sockObj.close()

for i in range(1):
    threading.Thread(target=run, args=(i,)).start()
