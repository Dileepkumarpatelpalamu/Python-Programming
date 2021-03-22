class Student:
    increament = 0.10
    @classmethod
    def growthsalary(cls,amount):
        return (cls.increament+1)*amount
    def getamount(self):
        self.pay = float(input("Basic salary is : "))
if __name__=='__main__':
    obj = Student()
    obj.getamount()
    growth=Student.growthsalary(obj.pay)
    print("Growth Salary : ",growth)
    # Implementation of Decorator in python
    def decor(num):
        def inner():
            a = num()
            add = a+10
            return add
        return inner
    @decor
    def num():
        return 20
    print(num())
