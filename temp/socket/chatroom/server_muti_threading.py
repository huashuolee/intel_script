import socket,os,threading
HOST = ''
PORT = 8001
MAX = 10

class chatroom():


    def interaction(self,conn,addr):
	while 1:
	    data = conn.recv(1024)
	    print 'receive ',data, ' from ', addr
	    if data == 'exit' or data == '':
		print addr, ' disconnect'
		break
	conn.sendall('Bye')
	conn.close()
		


    def new(self):
	s  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind((HOST,PORT))
	s.listen(5)
	while 1:
	    conn,addr = s.accept()
	    print addr, "connected" 
	    client_thread = threading.Thread(target=self.interaction, args=(conn,addr))
	    client_thread.start()




if __name__ == "__main__":
    chat = chatroom()
    chat.new()
