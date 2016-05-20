import socket

HOST = "localhost"
PORT = 8001

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))
client.sendall('-----------')
data = client.recv(1024)
client.close()
print 'Receive:', repr(data)

