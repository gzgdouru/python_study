import time, sys
from select import select
from socket import socket, AF_INET, SOCK_STREAM

myHost = ""
myPort = 50007
numPortSocks = 2

mainSocks = []
readSocks = []
writeSocks = []

def now():
    return time.ctime()

for i in range(numPortSocks):
    portSock = socket(AF_INET, SOCK_STREAM)
    portSock.bind((myHost, myPort))
    portSock.listen(5)
    mainSocks.append(portSock)
    readSocks.append(portSock)
    myPort += 1

print "select_server loop starting"
while True:
    readables, writeables, execptions = select(readSocks, writeSocks, [])
    for sockObj in readables:
        if sockObj in mainSocks:
            newSock, address = sockObj.accept()
            print "connect:", address, id(newSock)
            readSocks.append(newSock)
        else:
            data = sockObj.recv(1024)
            print "\tgot", data, "on", id(sockObj)
            if not data:
                sockObj.close()
                readSocks.remove(sockObj)
            else:
                reply = "Echo=>%s at %s" % (data, now())
                sockObj.send(reply)

