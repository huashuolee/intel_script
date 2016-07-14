import Queue
import threading

import time


class MyThread(threading.Thread):
    def __init__(self, myqueue,arg):
        self.myqueue = myqueue
        self.arg = arg
        threading.Thread.__init__(self)

    def run(self):
        print self.getName()
        while True:
            if myqueue.qsize > 0:
                myqueue.get()(self.arg)

def test(num):
    print str(num)+"\n"


if __name__=="__main__":
    myqueue = Queue.Queue(maxsize=2)
    for i in xrange(5):
        myqueue.put(test)
        MyThread(myqueue,5).start()

