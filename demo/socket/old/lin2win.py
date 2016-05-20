import socket,time

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect(("10.238.225.227",8001))
for i in range(10):
    socket.send(str(i))
    time.sleep(2)
socket.close()
