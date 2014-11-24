import threading
import time

def worker():
    print "workder"
    time.sleep(1)

for i in xrange(5):
    t=threading.Thread(target=worker)
    t.start()
print "".format(threading.activeCount())
