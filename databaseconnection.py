import mysql.connector as msc
class Connection:
    def __init__(self):
        self.conn= msc.connect(host = "localhost", user = "root",passwd = "DTGpalamu03#", database="Student")
        if not self.conn:
            print("Not Connected")
    def showdatabase(self,rec):
        self.cur= self.conn.cursor()
        qry="select * from " + rec
        dbs=self.cur.execute(qry)
        for i in self.cur:
            for j in range(len(i)):
                print(i[j],end="  ")
            print()
        self.cur.close()
    def insertdata(self,id,name,age,sal,sex):
        self.cur= self.conn.cursor()
        
if __name__=='__main__':
    con=Connection()
    rec= input("Enter Table Name To Select :")
        con.showdatabase(rec)
    