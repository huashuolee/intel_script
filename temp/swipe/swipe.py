import threading,os
def swipe():
    cmd = 'adb shell input swipe 500 200 200 200'
    os.system(cmd)

while True:
    th = threading.Thread(target=swipe)
    th.start()
