import SocketServer
from conf import GREETING, BAD_WORDS,GOOD_WORDS
from model.chat_history import ChatHistory
import time

class Myserver(SocketServer.BaseRequestHandler):
    def setup(self):
        pass
    def handle(self):
        conn=self.request
        #
        conn.send(GREETING)
        print GREETING
        receiver=conn.recv(1024).split()[-1]
        conn.send(receiver+' nice to meet you.')
        sender='chicken'
        history_list=list()
        
        while True:
            print "-----"
            data=conn.recv(1024)
            timestamp=time.asctime()
            
            chat_history_item=(receiver,sender,data,timestamp)
            history_list.append(chat_history_item)
            if 'exit' in data:
                conn.sendall('exit')
                break
            data=data.split()
            
            for word in data:
                if word in BAD_WORDS:
                    content='fuck off'
                elif word in GOOD_WORDS:
                    content='Thank you'
                else:
                    content='I do not understand'
            conn.sendall('chicken:'+content)
            
            chat_history_item=(sender,receiver,content,timestamp)
            history_list.append(chat_history_item)
            
        #
        chat_history=ChatHistory()
        chat_history.Add_Chat_History(history_list)
        conn.close()
    def finish(self):
        pass
    
if __name__=='__main__':
    ip_port=('127.0.0.1',9999)
    server=SocketServer.ThreadingTCPServer(ip_port,Myserver)
    server.serve_forever()       