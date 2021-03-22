import MySQLdb
class DatabaseEmployee:
    def __init__(self):
        self.host="localhost"
        self.user='root'
        self.password= "DTGpalamu03#"
        self.db="student"
        self.conn = MySQLdb.connect(self.host,self.user,self.password,self.db)
    def createCursor(self):
        self.cursor = self.conn.cursor()
    def CloseConnection(self):
        self.status=self.conn.close()
    def CreateTable(self):
        sqlqry ="""CREATE TABLE mysqldb (Id int, Name varchar(30) Not Null, Jobs varchar(20), Salary int, Sex char(5),primary key(Id))"""
        status=self.cursor.execute(sqlqry)
    def GetEmpData(self):
        self.eid=int(input("Enter Employee ID : "))
        self.name= input("Enter Employee Name : ")
        self.jobs= input("Enter Employee Job Role : ")
        self.salary= int(input("Enter Employee Salary : "))
        self.sex= input("Enter Employee Gender :")
        return self.eid,self.name,self.jobs,self.salary,self.sex
    def InsertData(self,eid,name,jobs,salary,sex):
        sqlqry="""INSERT INTO mysqldb values('%d','%s','%s','%d','%s')"""%(eid,name,jobs,salary,sex)
        status = self.cursor.execute(sqlqry)
        self.conn.commit()
    def ShowEmpData(self,subqry=''):
        sqlqry= """ SELECT * FROM mysqldb """+ subqry
        self.cursor.execute(sqlqry)
        data = self.cursor.fetchall()
        for row in range(len(data)):
            for col in range(len(data[row])):
                print(data[row][col],end="\t")
            print()
    def SearchEid(self):
        eid= int(input("Enter Employee ID to be search : "))
        subqry = "Where Id = %d"%(eid)
        self.ShowEmpData(subqry)
if __name__=='__main__':
    e1 = DatabaseEmployee() #This object is use for create connection python and mysql server 
    e1.createCursor()       # function is use for create cursor
    #eid,name,jobs,salary,sex=e1.GetEmpData() # This command is use for input data
    #e1.InsertData(eid,name,jobs,salary,sex)  # This function use for insert data in mysql server
    e1.SearchEid() # This function for display employee Details
    #e1.ShowEmpData() # This function is use for display all record from table
    e1.CloseConnection()                     # This function use for close connection
