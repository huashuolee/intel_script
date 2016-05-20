import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',8001))
while 1:
    data,addr = s.recvfrom(1024)
    print "Received:",data," from ", addr
    if data == "exit":
        s.close()
        break
