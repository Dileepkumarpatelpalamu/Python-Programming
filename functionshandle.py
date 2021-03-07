"""==============================Functions:=========================================================================
Function or Method - Function is the set of instructions to perform specific task. when it call the then code of block
is excuted. that means declare one time but call it many time. code is useable many time. In python is function object.
There are two types of functions or method:
1. pre-defined function example like type(),id(),len(),lower(),upper() etc
2. user defined function- A function is defined by programmer or user know as user defined function .
-- To create user defined function syntax is blew:
Syntax:----
    def functionName(arguments/parameters):
        -------------------------
        --------------------------
-- To call any function as syntax below:
Synatx----
    functionName(arguments/parameters) Note arguments are optional
-- Function return default type is None
example 
    def Add(a,b):
        c=a+b
        print("Sum=",c)
"""
# First we write code for define a function above
# def Add(a,b):
#     c=a+b
#     print("Sum=",c)
#Write code for call Add function like below:
# __name__==__main__ is the main function like c, c++ also java
# if __name__=="__main__":
#     d =Add(10,20)
#     Add(20.5,2.89)
#     Add("Hello ","World")
#     print(d)
# Otput of Fucntion is below:
# Sum= 30
# Sum= 23.39
# Sum= Hello World
# None # It show default function return type is None
"""====== Passing Parameters/ Arguments with functions in python=======================
In python there are four types of parameters or arguments
1. required parameters or arguments
    Above function Add(a,b) are required paramenters, if you do not pass value a and b the function generates errors
    so, it is call required function
2. default parameters or argumentss
    def Add(a,b=10):
        c = a+b
        print("Sum=",c)
    Above example Add(a,b=10) where a is required parameters and b is default parameters
    if we call above function without second parameter the default value is taken.
    Note:--- All the required parameters is before the default parameters,
        def Add(a=10,b) // generate error
        def Add(b,a=10) // Correct syntax of default parameters
3. named parameters or keyword parameters
    def connect(loc,uname,pwd,port,dbname,tname):
        print("Location :",loc)
        print("User name :",uname)
        print("Password :",pwd)
        print("Port no :",port)
        print("Database :",dbname)
        print("Table :",tbname)
4.  Arbitrary parameters: 
    def printrecord(*args,**kargs):
        for item in args:
            print(item)
        for k, v in kargs.items():
            print(k,":",v)
    if __name__=="__main__":
        connect(uname='satya',port=1521,pwd='satya123',tname='empdetails',dbname='employee',loc='127.0.0.1')
    Above example loc,uname,pwd,port,dbname,tname are called named/ keyword arguments
4. arbitatry paraments or arguments
"""
def connect(loc,uname,pwd,port,dbname,tname):
        print("Location :",loc)
        print("User name :",uname)
        print("Password :",pwd)
        print("Port no :",port)
        print("Database :",dbname)
        print("Table :",tname)
#Write a program to Decimal to binary Number
def binary(num):
    binno =""
    while num!=0:
        r=num%2
        binno = binno+str(r)
        num=num//2
    print("Binary Value :",binno[::-1])
def students(*name):
    for item in name:
        print("Hello ",item," have a nice day !!!!!!")
# example of args and kargs parameters 
def dataprint(*args,**kargs):
    for item in args:
        print(item)
    for k,v in kargs.items():
        print(k,':',v)
def mean():
    try:
        num = int(input("Enter no to element :"))
        data=[]
        for i in range(num):
            data.append(int(input("Enter "+str(i+1)+"/"+str(num)+" Element : ")))
        print("Avarage of Element :",sum(data)/len(data))
    except ValueError:
        print("Do not enter string :")
def printmsg(name,msg):
    print("Hello, ",name,msg)
"""----------------Lambda function-----------------------------------------------------
Lambda function :-
A lambda function is a single-line function declared with no name, which can have any number of arguments, but it can
only have one expression.
Syntax of lambda function:
    variable_name = lambda arg1,arg2......argn : expression
    example
    add = lambda x: x*x
    Calling for lambda function 
    add(10),add(15) etc
    by default lambda function return result of expression
-------------------Higher Order function------------------------------------------------
Higher order function :-
A function is called Higher Order Function if it contains other functions as a parameter or returns a function as 
an output i.e, the functions that operate with another function are known as Higher order Functions. ... Python too 
supports the concepts of higher order functions
There are following function higher order function:-
    1. sort()
    example
    l = ['java','python','hadoop','oracle']
    l.sort(key=lambda s:len(s))
    print(l)
    2. filter()- 
    The filter() method constructs an iterator from elements of an iterable for which a function returns true. In 
    simple words, filter() method filters the given iterable with the help of a function that tests each element in 
    the iterable to be true or not.
    synatx :
    object = filter(lambda function, list object)
    example
    res = tuple(filter(lambda a : a%2==0,[1,2,3,4,5,6,7,8,9]))
    print(res)
    3. map() function:-
    map() function executes a specified function for each item in an iterable. The item is sent to the function as 
    a parameter
    syntax :
    object = map(lambda function,list object)
    example
    l = ['python','Java','hadoop']
    m = map(lambda s: s.upper(),l)
    for item in m:
        print(item)
    4. reduce() function:-
    reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list
    elements mentioned in the sequence passed along. This function is defined in “functools” module. Working :
    At first step, first two elements of sequence are picked and the result is obtained. first step import functools with
    'from functools import reduce'
    syntax :
    object = reduce(lambda function, list object)
    example
    total = reduce(lambda a,x: a+x,[10,2,3,8,7,7])
    print("sum=",total)
recursion function :
This means that the function will continue to call itself and repeat its behavior until some condition is met to 
return a result
 syntax of recurtion function :
 def functionname():
     --------------
     --------------
     --------------
     functionname()
example of recurtion function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
nested function :-
A nested function is simply a function within another function, and is sometimes called an "inner function". There 
are many reasons why you would want to use nested functions
syntax :
def add():
    def printmsg():
        print("You are within inner function)
    printmsg()
    print("you are present outer function")
add()
example 
x=99
def f1():
    x=88 
    def f2():
        print("x value inside f2 ,x)
    f2()
    print("x value inside f1,x)
def f3():
    print("x value inside f3,x)
Global variable:
Global Variables In Python, a variable declared outside of the function or in global scope is known as a global 
variable. This means that a global variable can be accessed inside or outside of the function. 
local variable :
A variable declared inside the function's body or in the local scope is known as a local variable.
if you want make local variabe to create global using global keyword
exampl
def myfunction():
    global a
    a =100
that means a is the global variable
"""
# Write a code for lambda function
#a = lambda x: x*x
#l = ['java','python','c','hadoop','oracle']
#l.sort(key=lambda s:len(s))
#['c', 'java', 'python', 'hadoop', 'oracle']
#l.sort(key=lambda s:len(s),reverse=True)
#['python', 'hadoop', 'oracle', 'java', 'c']
#print(l)
#below example of filter() method
#res = tuple(filter(lambda a : a%2==0,[1,2,3,4,5,6,7,8,9]))
#print(res)
#(2, 4, 6, 8)
# res=filter(lambda a : a%2==0,[1,2,3,4,5,6,7,8,9])
# for item in res:
#     print(item)
# res= filter(lambda a: a%2!=0,[15,12,5,7,9,50])
# for i in res:
#     print(i)
# example of map() function
# l = ['python','Java','hadoop']
# m = map(lambda s: s.upper(),l)
# for item in m:
#     print(item)
# for item in map(lambda s:s.upper(),['java','Python','Oracle']):
#     print(item)
#example to reduce function
# from functools import reduce
# total = reduce(lambda a,x: a+x,[10,2,3,8,7,7])
# print("sum=",total)
# nested function 
x=99
def f1():
    x=88 
    def f2():
        print("x value inside f2",x)
    return f2
    print("x value inside f1", x)
def f3():
    print("x value inside f3",x)
# example of recurtion function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
## Main function declare in Python Like
if __name__=="__main__":
    pass
    #print(factorial(5))
    # call this types inner function call in python
    #f = f1()
    #f()
    #connect(uname='satya',port=1521,pwd='satya123',tname='empdetails',dbname='employee',loc='127.0.0.1')
    #binary(20)
    #emplist=['Rohit','Maya','Salini','Mohit','Gandhi']
    #students(*emplist)
    #dataprint(20,50,100,2000)
    #dataprint(10,20,30,40,{'name':'Mahesh','College':'Gla College'})
    #dataprint(eid=101,name='Dileep',mobile='8409900949',salary=15000)
    #mean()
    #print(a(5))
    # l=['Python,','Java','C','C++','net','hadoop']
    # l.sort(key=lambda s:len(s))
    # print(l)
    # printmsg(msg='good morning',name='Mohan')
    # printmsg(name='Dileep',msg="Good night")
    # printmsg('Gagan','Welcome to palamu')
    # printmsg('Maya',msg='Happy birthday')
    #printmsg(msg='Welcome to Hydrabas','Rohit') #Error