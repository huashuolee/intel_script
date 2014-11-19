import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('',8001))
socket.listen(10)
while True:
    conn,addr = socket.accept()
    conn.settimeout(3000)
    buf = conn.recv(1024)
    print buf
