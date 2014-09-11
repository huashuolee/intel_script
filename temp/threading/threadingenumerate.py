import threading
import time

def worker():
    print "worker"
    time.sleep(1)
    return

threads = []
for i in xrange(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
for item in threading.enumerate():
    print item
for item in threads:
    print item

print "current has {} threads".format(threading.activeCount())
