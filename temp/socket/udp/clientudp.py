import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 8001
host = 'localhost'
while 1:
    msg = raw_input('input:\n')
    s.sendto(msg,(host,port))
    if msg == "exit":
        s.close()
        break
