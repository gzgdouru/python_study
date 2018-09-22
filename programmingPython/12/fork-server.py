import os
import sys
import time
from socket import *
import signal

myHost = ""
myPort = 50007

sockObj = socket(AF_INET, SOCK_STREAM)
sockObj.bind((myHost, myPort))
sockObj.listen(5)


def now():
    return time.ctime(time.time())

activeChildren = []

def reapChildren():
    while activeChildren:
        pid, stat = os.waitpid(0, os.W_OK)
        if not pid: break
        activeChildren.remove(pid)

def handleClient(connection):
    time.sleep(5)
    while True:
        data = connection.recv(1024)
        if not data: break
        reply = "Echo=>%s at %s" % (data, now())
        connection.send(reply)
    connection.close()
    os._exit(0)

def dispatcher():
    while True:
        connection, address = sockObj.accept()
        print "server connected by", address,
        print "at", now()
        reapChildren()
        childPid = os.fork()
        if childPid == 0:
            handleClient(connection)
        else:
            activeChildren.append(childPid)

dispatcher()