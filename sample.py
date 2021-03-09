"""
-----------------Encapsulation
Encapsulation in Python is the process of wrapping up variables and methods into a single entity.
"""
class Sample: pass
class Employee:
    def __init__(self,name,jobs,salary):
        self.name=name
        self.jobs=jobs
        self.salary=salary
    def empinfo(self):
        return self.name,self.salary,self.jobs
if __name__=='__main__':
    Sample.x=10
    Sample.y=20
    a = Sample()
    b = Sample()
    print('Sample :',Sample.x)
    print('a :',a.x)
    print('b',b.x)
    a.x=20
    a.y=25
    print('Sample items :',Sample.__dict__.items())
    print('Sample Keys :',Sample.__dict__.keys())
    print('a items :',a.__dict__.items())
    print('a Keys :',a.__dict__.keys())
    print('a values :',a.__dict__.values())
    print('b items :',b.__dict__.items())
    print('a values x :',a.__dict__['x'])
    print('a value y :',a.__dict__['y'])
    #print(b.__dict__['x']) # KeyError :'x'
    myobject = Employee('Dileep',"['Python','Django']",5000)
    name,jobs,salary=myobject.empinfo()
    print(name,"\t",jobs,'\t',salary) 













