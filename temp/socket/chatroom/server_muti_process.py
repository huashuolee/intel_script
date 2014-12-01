# how to kill process


import socket,os,threading
import multiprocessing as mul

HOST = ''
PORT = 8001
MAX = 10

class chatroom():
    def __init__(self):
        print "chat start....\n"
	
    def interaction(self,conn,addr):
        print self.plist
	while 1:
	    data = conn.recv(1024)
	    print 'receive ',data, ' from ', addr
	    if data == 'exit' or data == '':
		print addr, ' disconnect'
		break
	conn.sendall('Bye')
	conn.close()

    def new(self):
	plist = []
	s  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind((HOST,PORT))
	s.listen(5)
	while 1:
	    conn,addr = s.accept()
	    print addr, "connected" 
	    client_process = mul.Process(target=self.interaction, args=(conn,addr))
	    client_process.start()
	    plist.append(client_process)
	    #for item in plist:
	    #	print item
	    #	item.join()






if __name__ == "__main__":
    chat = chatroom()
    chat.new()
