class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
        return f"Person :{self.name} Job: {self.job} Salary : {self.pay}"
        #return '[Person: %s,%s, %s]' % (self.name, self.job, self.pay)
class Manager(Person):
    def __init__(self,name,pay):
        Person.__init__(self, name, 'mgr', pay)
    def giveRaise(self, percent, bonus=.10): # Redefine at this level
        Person.giveRaise(self, percent + bonus) # Call Person's version
class Department:
    def __init__(self,*args):
        self.members= list(args)
    def addMembers(self,obj):
        self.members.append(obj)
    def giveRaise(self,percent):
        for obj in self.members:
            obj.giveRaise(percent)
    def showall(self):
        for obj in self.members:
            print(obj)
if __name__ == '__main__':
    pass
    


