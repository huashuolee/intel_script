import uiautomator
import os
import time

d = uiautomator.Device()

for i in xrange(100):
    print i
    d.press.camera()
    time.sleep(2)
    d(className = "android.widget.FrameLayout").swipe.left()
    time.sleep(2)
    d.click(525, 324)
    time.sleep(2)
    d(className = "android.widget.FrameLayout").swipe.right()
    d(className = "android.widget.FrameLayout").swipe.right()
    time.sleep(1)
    d(className = "android.widget.FrameLayout").swipe.right()
print "Done"
