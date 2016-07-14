import threading


class MyThread(threading.Thread):
    def __init__(self):

        threading.Thread.__init__(self)
        self.start()


    def run(self):
        print "begin to run"



MyThread()
