import threading
import time

def worker():
    print "workder"
    time.sleep(1)
    return

if __name__ =="__main__":
    for i in xrange(5):
        worker()
print "".format(threading.activeCount())
