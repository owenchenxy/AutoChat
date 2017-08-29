import MySQLdb

class MySQLHelper(object):
    def __init__(self,db):
        self.__db=db
    def Modify_Table_One(self,sql,params):
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='emc123123',db=self.__db)
        cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        
        reCount=cur.execute(sql,params)
        
        conn.commit()
        
        cur.close()
        conn.close()
    def Modify_Table_Many(self,sql,params):
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='emc123123',db=self.__db)
        cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        
        reCount=cur.executemany(sql,params)
        
        conn.commit()
        
        cur.close()
        conn.close()
    def Get_Data_Dict(self,sql,params):
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='emc123123',db=self.__db)
        cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        
        reCount=cur.excute(sql,params)
        data=cur.fetchall()
        
        cur.close()
        conn.close()
        return data
    
    def Get_Data_One(self,sql,params):
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='emc123123',db=self.__db)
        cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        
        reCount=cur.execute(sql,params)
        data=cur.fetchone()
        
        cur.close()
        conn.close()
        return data