import threading
import time

def worker():
    print "worker"
    time.sleep(1)

for i in xrange(5):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()
    print "daemon"
print "current has {} threads".format(threading.activeCount())
