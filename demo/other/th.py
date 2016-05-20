import time
import thread

def runner(arg):
    for i in range(6):
        print str(i)+':'+arg

        time.sleep(1)
    #......
    thread.exit_thread()  #...thread.exit()
       
#.................
#........tuple...........
thread.start_new_thread(runner, ('hello world',))   #...thread.start_new(runner, ('hello world'))

#..........................
lock = thread.allocate_lock()  #...thread.allocate()
num = 0
#........True.....False
if lock.acquire():
    num += 1
    #...
    lock.release()
#thread...............................
time.sleep(10)
print 'num:'+str(num)

