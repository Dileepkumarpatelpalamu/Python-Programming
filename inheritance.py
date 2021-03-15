class Persons:
    def __init__(self):
        self.name=input("Enter name : ")
        self.salary= float(input("Enter salary : "))
    def getdisplay(self):
        print("Name : ",self.name)
        print("Salary : ",self.salary)
    def __repr__(self):
        return f"Name :{self.name} \t Salary : {self.salary}"
    def __str__(self):
        return "Hello python developer I wish you to long life"
class Emp:
    def __init__(self):
        self.eid = int(input("Enter Employee id : "))
        self.name= input("Enter Employee name :")
    def __repr__(self):
        return ("eid =%d\nename=%s"%(self.eid,self.name))
class Client:
    def __init__(self):
        self.id = int(input("Enter Client ID : "))
        self.name = input("Enter Client Name : ")
        self.mobile= input("Enter Client contact no : ")
        self.address = input("Enter Client Address : ")
        self.email = input("Enter Client email : ")
class Bank(Client):
    def getaccount(self):
        self.accountno = int(input("Enter account no : "))
        self.amount = int(input("Enter amount : "))
    def getdeposite(self,deposite):
        self.amount = self.amount + deposite
    def getwithdraw(self,withdraw):
        if self.amount >= withdraw:
            self.amount = self.amount - withdraw
        else:
            print("your account have insufficient balance")
    def accountstmt(self):
        for key,value in self.__dict__.items():
            print(key,'\t',value)
class Student(Client):
    def getmarks(self):
        self.english=int(input("Enter English Marks : "))
        self.math=int(input("Enter Maths Marks : "))
        self.science=int(input("Enter Science Marks : "))
        self.socialscience=int(input("Enter Social Science Marks : "))
        self.Computer=int(input("Enter Computer Marks :"))
    def getcalculate(self):
        self.total=self.english+ self.math+self.science+self.socialscience+self.Computer
        self.percentage= self.total / 5
        if self.english <33 or self.math<33 or self.science<33 or self.socialscience<33 or self.Computer<33 or self.percentage<33:
            self.result="Fail!! Dont worry Try again"
        elif self.percentage>=75:
            self.result="you are passed with Distinct Marks"
        elif self.percentage>=60 and self.percentage<75:
            self.result="you are passed with First Division Marks"
        elif self.percentage>=45 and self.percentage<60:
            self.result="you are passed with Second Division Marks"
        elif self.percentage>=33 and self.percentage<75:
            self.result="you are passed with Third Division Marks"
        else:
            self.result="Fail!! Dont worry Try again"
    def displayresult(self):
        for key,value in self.__dict__.items():
            print(key,'\t:',value)
if __name__=='__main__':
    pass
