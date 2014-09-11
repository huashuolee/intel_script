import multiprocessing as mul

def proc1(pipe):
    pipe.send('hello')
    print ('proc1 rec:', pipe.recv())

def proc2(pipe):
    pipe.send('hello, too')
    print ('proc2 rec:', pipe.recv())

pipe = mul.Pipe()

p1 = mul.Process(target=proc1, args=(pipe[0],))
p1.start()
p2 = mul.Process(target=proc2, args=(pipe[1],))
p2.start()
