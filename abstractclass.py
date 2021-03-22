from abc import ABCMeta,abstractmethod
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def getdata(self): pass
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self):pass
class Circle(Shape):
    def getdata(self):
        self.radius= float(input("Enter radius of circle : "))
    def area(self):
        print("Area of Circle : ",round((3.14*self.radius**2),2))
    def perimeter(self):
        print("Perimeter of Circle : ",round((2*3.14*self.radius),2))
class Rect(Shape) :
    __mydata = 200
    def getdata(self):
        self.l= float(input("Enter length of rectangle : "))
        self.b= float(input("Enter width of rectangle : "))
    def area(self):
        print("Area of Rectangle : ",round((self.l*self.b),2))
    def perimeter(self):
        print("Perimeter of Rectangle : ",round(2*(self.l+self.b),2))
if __name__=='__main__':
    e1= Rect()
    e1.getdata()
    e1.area()
    e1.perimeter()
