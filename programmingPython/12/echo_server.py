import socket
import time

myHost = ""
myPort = 50007

sockObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockObj.bind((myHost, myPort))
sockObj.listen(5)

while True:
    connection, address = sockObj.accept()
    print "server connected by", address
    while True:
        data = connection.recv(1024)
        time.sleep(3)
        if not data: break
        connection.send("Echo=>" + data)
    connection.close()