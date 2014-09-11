import subprocess,os,time
from multiprocessing import Process
from threading import Thread

def kill_logcat():
    cmd = 'adb shell ps '
    p = subprocess.Popen(cmd, shell=True, stdout= subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    process_list = stdout.split('\n')
    for item in process_list:
        if "logcat" in item:
            pid = item.split()[1] 
            cmd = 'adb shell kill -9 ' + str(pid)
            os.system(cmd)
 
def capture():
    os.system('adb shell input keyevent 27')

def start_capture():
    for i in xrange(10):
        th = Thread(target=capture)
        time.sleep(0.333)
        th.start()

def sand_keyevent():
    pass

def analyze_log():
    cmd = "grep -nr latency: log "
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    for item in stdout.strip().split('\r\n'):
        latency = item.split(':')[-1].split()[0]
        print "shot2shot latency: {}".format(latency)
    
def get_log():
    os.system("adb logcat -c")
    time.sleep(1)
    os.system("adb logcat -v time > log")

def enable_log():
    cmd = "adb wait-for-device root"
    os.system(cmd)
    cmd = "adb wait-for-device remount"
    os.system(cmd)
    cmd = "adb wait-for-device shell setprop camera.hal.perf 3"
    os.system(cmd)
    time.sleep(1)

if __name__=="__main__":
    enable_log()
    p = Process(target=get_log)
    p.start()
    print "start get log"
    print p.pid
    #start_capture()
    time.sleep(10)
    p.terminate()
    kill_logcat()
    print "ending get log"
    analyze_log()

