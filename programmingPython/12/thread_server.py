import thread
from socket import *
import time

myHost = ""
myPort = 50007

sockObj = socket(AF_INET, SOCK_STREAM)
sockObj.bind((myHost, myPort))
sockObj.listen(5)

def now():
    return time.ctime(time.time())

def handleClient(connection):
    time.sleep(5)
    while True:
        data = connection.recv(1024)
        if not data: break
        reply = "Echo=>", data
        connection.send(data)
    connection.close()

def dispatcher():
    while True:
        connection, address = sockObj.accept()
        print "server connected by", address,
        print "at", now()
        thread.start_new_thread(handleClient, (connection,))

dispatcher()