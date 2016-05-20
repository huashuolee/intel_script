import os 
import time
import subprocess
from multiprocessing import Process


def kill_logcat():
    cmd = 'adb shell ps -ef'
    p = subprocess.Popen(cmd, shell=True, stdout= subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    process_list = stdout.split('\n')
    for item in process_list:
        if "logcat" in item:
            pid = item.split()[0] 
            cmd = 'adb shell kill -9 ' + str(pid)
            print cmd
            os.system(cmd)
         

def enablelog():
    os.system('adb wait-for-device root')
    os.system('adb wait-for-device remount')
    os.system('adb wait-for-device shell setprop camera.hal.perf 1')

def launchcamera():
    cmd = "adb shell am start -n com.android.camera2/com.android.camera.CameraLauncher"
    os.system(cmd)

def getlog():
    cmd = 'adb logcat -c'
    os.system(cmd)
    print "Done"    
   # cmd = "adb shell am start -n com.android.camera2/com.android.camera.CameraLauncher"
   # os.system(cmd)
    cmd = 'adb logcat -v time > log'
    os.system(cmd)

def analyzelog():
    # get the start time timestamp
    try:
        cmd = 'grep -nr "START" log'
        p =subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        stdout, stderr = p.communicate()
        m = stdout.split(':')[2]
        s= stdout.split(':')[3].split()[0]
        starttime = float(m)*60 + float(s)
    except IndexError:
        print "can't find START in the log, check whether perf 1 is enabled."
  
    # get the end time timestamp
    try:
        cmd = 'grep -nr "1st" log'
        p =subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        stdout, stderr = p.communicate()
        m = stdout.split(':')[2]
        s= stdout.split(':')[3].split()[0]
        endtime = float(m)*60 + float(s)
    except IndexError:
        print "Can't find 1st in the log, check perf 1 is enabled."

    # calc the latency
    try:
        latency = (endtime - starttime)*1000
        print "The launch2preview latency: {}  ms ".format(latency)
    except:
        print "error, pls check the log"
   
if __name__ =='__main__':
    enablelog()
    p = Process(target = getlog)
    p.start()
    print p.pid
    time.sleep(10)
    p.terminate()
    kill_logcat()
    analyzelog()



