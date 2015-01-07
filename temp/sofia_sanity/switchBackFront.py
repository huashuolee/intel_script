import os,time

cmd_settings = 'adb shell input tap 881 176'
cmd_switch = 'adb shell input tap 607 361'

for i in xrange(100):
    print i
    os.system(cmd_settings)
    time.sleep(2)
    os.system(cmd_switch)
    time.sleep(2)
print "Done"


