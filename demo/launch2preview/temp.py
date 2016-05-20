from multiprocessing import Process
import os

def f():
    os.system('adb logcat -v time |tee log1') 

if __name__ =="__main__":
    p =Process(target=f)
    p.start()
    p.join()
