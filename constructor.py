class Emp:
    def __init__(self):
        self.id=int(input("Enter employee id :"))
        self.name= input("Enter employee Name : ")
        self.salary=float(input("Enter employee salary :"))
    def showemp(self):
        print("Emp ID :",self.id)
        print("Emp Name : ",self.name)
        print("Emp Salary : ",self.salary)
    def getlast(self):
        return self.name.split()[-1]
    def salaryupdate(self,inc):
        return round(self.salary*(1+inc),2)
    def getfirst(self):
        return self.name.split()[0]
class Mobile:
    def __init__(self):
        self.company= input("Enter Company Name : ")
        self.model= input("Enter model : ")
        self.processor= input("Processor Types :")
        self.price = float(input("Enter price : "))
    def getmodel(self):
        return self.model
    def getcompany(self):
        return self.company
    def getprice(self):
        return self.price
    def getprocessor(self):
        return self.processor
    def getdisplay(self):
        while True:
            print(""" 
                1. Get Company 
                2. Get Model
                3. Get Processor
                4. Get Price
            """)
            choice=(input("Enter your choice : [To Exit press: Q]: "))
            if choice.upper() =='Q':
                break
            elif choice=='1':
                print('Company : ',self.getcompany())
            elif choice == '2':
                print('Model : ',self.getmodel())
            elif choice =='3':
                print('Processor : ',self.getprocessor())
            elif choice=='4':
                print('Price : ',self.getprice())
            else:
                print("Enter valid choice :")
if __name__=='__main__':
    phone = Mobile()
    phone.getdisplay()
    