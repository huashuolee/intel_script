import socket,os
HOST = ''
PORT = 8001


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(5)

while 1:
    conn,addr = server.accept()
    print addr, "connected" 
    while 1:
        data = conn.recv(1024)
        print "receive ",data, "  from " ,addr
        if data == "exit" or data == "":
            print addr , ' disconnect'
            break
        conn.sendall('done')
    conn.sendall("Bye")
    conn.close()

