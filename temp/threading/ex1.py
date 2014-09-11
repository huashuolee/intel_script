import threading
import time

class MyThread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        for i in range(10):
            print self.getName(), i
            time.sleep(1)


t1 = MyThread('t1')
t1.start()
