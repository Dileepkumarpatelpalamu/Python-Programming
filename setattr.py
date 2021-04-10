# Write a program to exetute __getattr__ , __setattr__ and with __repr__ builtins function
class Employee:
    def __getattr__(self,name):
        if name =='ename':
            return self.__dict__['_ename']
        elif name =='jobs':
            return self.__dict__['_jobs']
        elif name =='age':
            return self.__dict__['_age']
        else:
            raise AttributeError(name)
    def __setattr__(self,name,value):
        if name=='age':
            if value>=18 and value<=30:
                self.__dict__['_age']=value
            else:
                print("Age should be between 18 to 30 !")
        elif name=='ename':
            if value.isalpha():
                self.__dict__['_ename']=value
            else:
                print("Name should be only string")
        elif name=='jobs':
            if value.isalpha():
                self.__dict__['_jobs']= value
            else:
                print("jobs should be only string")
        else:
            raise AttributeError(name)
    def __repr__(self):
        return f"Employee Name : %s \t Employee Location :%s \t Employee Age : %s"%(self.ename,self.jobs,self.age)
if __name__=='__main__':
    e1=Employee()
    e1.ename="DileepKumarPatel"
    e1.jobs="Hyderabad"
    e1.age=20
    print(e1)

    



        