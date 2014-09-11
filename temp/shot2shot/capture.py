from multiprocessing import Process
from threading import Thread
import os,time


def capture():
    os.system('adb shell input keyevent 27')

for i in xrange(10):
    th = Thread(target=capture)
    time.sleep(0.333)
    th.start()

