# how to kill process


import socket,os,threading
import multiprocessing as mul

HOST = ''
PORT = 8001
MAX = 10
def new_socket():
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

def listener():
    num = 1
    while num < MAX:
        s  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((HOST,PORT))
        s.listen(5)

        while 1:
            conn,addr = s.accept()
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
def interaction(conn,addr):
    while 1:
        data = conn.recv(1024)
        print 'receive ',data, ' from ', addr
        if data == 'exit' or data == '':
            print addr, ' disconnect'
            break
    conn.sendall('Bye')
    conn.close()
            


def new():
    plist = []
    s  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(5)
    while 1:
        conn,addr = s.accept()
        print addr, "connected" 
        client_process = mul.Process(target=interaction, args=(conn,addr))
        client_process.start()
        plist.append(client_process)




if __name__ == "__main__":
    t = threading.Thread(target=new)
    t.start()
