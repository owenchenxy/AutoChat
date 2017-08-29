import MySQLdb
from utility.sql_helper import MySQLHelper

class ChatHistory(object):
    def __init__(self):
        self.__db=MySQLHelper('chat_tool')
        
    def Get_All_History(self):
        sql='select * from chat_history'
        params=()
        return self.__db.Get_Data_Dict(sql, params)
    
    def Get_History_Sender(self,sender):
        sql='select * from chat_history where sender=%s'
        params=(sender)  
        return self.__db.Get_Data_Dict(sql, params) 
    
    def Add_Chat_History(self,history_list):
        sql='insert into chat_history(sender,receiver,content,time) value(%s,%s,%s,%s)'
        params=history_list
        self.__db.Modify_Table_Many(sql, params)