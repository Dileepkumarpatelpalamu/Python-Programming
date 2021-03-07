# class Student:
#     def __init__(self,lang,lan):
#         self.lang=lang
#         self.lan=lan
#     def liststring(self):
#         newstr=""
#         for ch in str(self.lan) :
#             if ch.isalpha() and ch in "Net" or ch.isspace():
#                     newstr=newstr + ch
#         return [self.lang[0]+newstr],self.lan
# if __name__=='__main__':
#     obj = Student(['Java Python'],['Hadoop Net'])
#     print(obj.liststring())

class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
    def scoops(self):
        data=[]
        for i in self.ingredients:
            my=[]
            for j in self.toppings:
                my.append(i)
                my.append(j)
            data.append(my)
        return data
if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]

