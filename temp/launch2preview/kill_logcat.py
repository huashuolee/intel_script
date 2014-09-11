import subprocess
import os

def kill_logcat():
    cmd = 'adb shell ps -ef'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    process_list = stdout.split('\n')
    for item in process_list:
        if "logcat" in item:
            pid = item.split()[0] 
            print pid
            cmd = 'adb shell kill -9 ' + str(pid)
            print cmd
            os.system(cmd)

 
if __name__=="__main__":
    kill_logcat()
