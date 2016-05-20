import multiprocessing
import time

p = multiprocessing.Process(target=time.sleep, args=(100,))
p.start()
print p.pid
