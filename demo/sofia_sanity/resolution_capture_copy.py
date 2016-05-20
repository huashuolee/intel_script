import uiautomator
import time

d = uiautomator.Device()

def settings():
    d.click(848 ,102)
    time.sleep(3)
    d.click(523,347)
    time.sleep(3)
    d.click(531,286)
    time.sleep(3)

# select different resolution and take picture
def capture(x,y):
    d.click(x,y) 
    time.sleep(3)
    d.press.camera()

       
position = [(587,130),(587,185),(587,280),(587,330),(587,420),(587,490),(587,570)]

for i in xrange(100):
    print i
    for item in position:
        settings()
	capture(int(item[0]),int(item[1]))
	time.sleep(3)
    settings()    
    d.swipe(587, 570, 587, 420)
    time.sleep(3)
    d.click(587,570)
    time.sleep(3)
    d.press.camera()
    time.sleep(3)
