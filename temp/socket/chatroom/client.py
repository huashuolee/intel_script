import socket

HOST = "localhost"
PORT = 8001
try:
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((HOST,PORT))
    client.sendall('-----------')
    while 1:
	client.sendall(raw_input('>>>'))
except:
    client.close()
    print '{}'.format('socket close')
