import threading
import time

def worker():
    print "worker"
    time.sleep(1)
    return

for i in xrange(5):
    t = threading.Thread(target=worker)
    t.start()
print "current has {} threads".format(threading.activeCount())
