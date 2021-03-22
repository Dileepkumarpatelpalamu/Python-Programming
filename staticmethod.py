class Automation:
    objectcounter = 0
    def __init__(self):
         Automation.objectcounter=Automation.objectcounter + 1
    @staticmethod
    def showobject():
        print("Count of object : ",Automation.objectcounter)
    @classmethod
    def getdata(cls):
        print("Class method called : ",cls.objectcounter)
if __name__=='__main__':
    obj1= Automation()
    obj2= Automation()
    obj3= Automation()
    obj4= Automation()
    obj1.showobject()
    obj1.getdata()
