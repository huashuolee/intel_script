import uiautomator, time

def switcher():
    d(resourceId='com.android.camera2:id/camera_switcher').click()
    time.sleep(2)

def select_photo():
    d(description='Switch to photo').click()
    time.sleep(2)

def select_video():
    d(description='Switch to video').click()
    time.sleep(2)

if __name__=="__main__":
    d=uiautomator.Device()
    for i in xrange(100):
        print i
	switcher()
	selectVideo()
	switcher()
	selectPhoto()
    print "done "
