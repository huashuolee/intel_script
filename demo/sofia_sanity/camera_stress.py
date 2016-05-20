import uiautomator
import time
import os
import sys

d = uiautomator.Device()

#if len(sys.argv)<2:
#    print "Usage: python camera_stress.py [image/video] "
#    sys.exit(0)
#if sys.argv[1]== "image":
#    cmd = "adb shell am start -n com.google.android.GoogleCamera/com.android.camera.CameraLauncher -a  android.media.action.STILL_IMAGE_CAMERA"
#    os.system(cmd)
#time.sleep(5)    

for i in xrange(100):
    d.press.camera()
    time.sleep(5)
    print i
print "Done"
