import os

def child():
    print "hello for child", os.getpid()
    os._exit(0)

def parent():
    while True:
        newPid = os.fork()
        if newPid == 0:
            child()
        else:
            print "hello for parent", os.getpid(), newPid

        if raw_input() == "q": break

parent()