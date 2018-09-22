import os
from multiprocessing import Process, Lock

def whoami(lable, lock):
    msg = "%s: name:%s, pid:%s"
    with lock:
        print msg % (lable, __name__, os.getpid())

if __name__ == "__main__":
    lock = Lock()
    whoami("function call", lock)

    p = Process(target=whoami, args=("spaured child", lock))
    p.start()
    p.join()

    str = "run process %s"
    for i in range(5):
        Process(target=whoami, args=((str % i), lock)).start()

    with lock:
        print "main process exit..."
