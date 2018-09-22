import os
from multiprocessing import Process, Pipe

def sender(pipe):
    pipe.send(["spam"] + [42, "eggs"])
    pipe.close()

def talked(pipe):
    pipe.send(dict(name = "Bob", spam = 42))
    reply = pipe.recv()
    print "talked got:", reply

if __name__ == "__main__":
    (parentEnd, childEnd) = Pipe()
    Process(target=sender, args=(childEnd,)).start()
    print "parent got:", parentEnd.recv()
    parentEnd.close()

    (parentEnd, childEnd) = Pipe()
    child = Process(target=talked, args=(childEnd,))
    child.start()
    print "parent got:", parentEnd.recv()
    parentEnd.send({x * 2 for x in "spam"})
    child.join()
    print "parent exit..."