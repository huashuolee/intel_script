import threading,time,os

def doChore():
    time.sleep(0.5)

def worker():
    print "worker\n"
    time.sleep(1)

class BoothThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        worker()


for k in xrange(5):
    new_thread = BoothThread()
    new_thread.start()
