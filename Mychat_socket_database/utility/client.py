import socket

class ChatClient(object):
    def __init__(self,name):
        self.name=name
    def start_session(self):
        client=socket.socket()
        ip_port=('127.0.0.1',9999)
        client.connect(ip_port)
        
        data=client.recv(1024)
        print data    #'Hello, my name is Chicken,what is your name?'
        client.send(self.name)
        print('my name is %s'%self.name)
        
        data=client.recv(1024)
        print data   #' nice to meet you.'
        while True:
            to_send=raw_input('%s:'%self.name)
            client.sendall(to_send)
            received=client.recv(1024)
            if received=='exit':
                break
            print received
        raw_input('\npress any key to close this session')
        client.close()

chat_client=ChatClient('owen')
chat_client.start_session()
       
        