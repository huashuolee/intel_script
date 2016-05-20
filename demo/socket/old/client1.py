import socket,time

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect(('localhost', 8001))
for i in range(10):
    print str(i)
    time.sleep(10)
    socket.send(str(i))
