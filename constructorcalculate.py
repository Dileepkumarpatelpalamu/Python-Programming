class Student:
    def __init__(self):
        self.name=input("Enter Student Name : ")
        self.english=int(input("Enter English number : "))
        self.maths=int(input("Enter Maths number : "))
        self.science=int(input("Enter Science number : "))
        self.social=int(input("Enter Social science number : "))
        self.comp=int(input("Enter Computer number : "))
    def getmarks(self):
        self.marks=(self.english+self.maths+self.science+self.social+self.comp)
        print(self.name," Total Marks :",self.marks)
    def getmaxmarks(self):
        self.sub=max(self.english,self.maths,self.science,self.social,self.comp)
        print("Maximum marks in Subject :",self.sub)
    def getminmarks(self):
        self.submin=min(self.english,self.maths,self.science,self.social,self.comp)
        print("Minimum marks in Subject :",self.submin)
    def getpercentage(self):
        self.percentage= round((self.marks/5),2)
        print(self.name," Percentage :",self.percentage)
    def getdivision(self):
        if self.percentage >= 75:
            self.result="Distinct Division"
        elif self.percentage<75 and self.percentage>=60:
            self.result= "First Division"
        elif self.percentage <60 and self.percentage >=45:
            self.result="Second Division"
        elif self.percentage <45 and self.percentage>=33:
            self.result= "Third Division"
        else:
            self.result="Fail don't worry try again !"
        print(self.name, " wish you to ",self.result)
if __name__=='__main__':
    s1= Student()
    s1.getmarks()
    s1.getpercentage()
    s1.getdivision()
    s1.getmaxmarks()
    s1.getminmarks()