"""===============================Exception Handling=================================================
Exceptions are event that can modify the flow of control through a program. In Python exceptions are triggered and
automatically interpreted by your code.
Exception handiling ->------------------------------
Python raise exceptions when even it detect error in program at runtime. you can catch and respond to the errors in
your code, or ignore the exceptions that are raised if an error is ignored. Python's default exception handling
behaviour kick in it stop the program and print on error message. if you don't want this default behaviour code a try
statement to catch and recieved from the exception python will jump to your try handler when the error is detected and your
will resume excution after the try block.
1. Default Exception Handler
    Suppose we write the following function
"""
def fetcher(obj,index):
    return obj[index]
x ="Master"
#print(fetcher(x,5))
#print(fetcher(x,6))
#IndexError: string index out of range
"""
Because our code does not explicitly catch this exception, if filters backup to the top level of the program and invoke the
exception handler which simply print the standard error message with stack trace a list of all the lines and function
that where active when the exception occured
                            if you don't want the default exception behaviour wrap the call in the try satement to catch
exceptions yourself.
In python few keyword to handles Exception handling-------
1. try
2. except
3. raise
4. finally
There are following class derived from Exception Class:
1. exception ArithmeticError
2. exception BufferError
3. exception LookupError
4. exception AssertionError
5. exception AttributeError
6. exception EOFError
7. exception FloatingPointError
8. exception GeneratorExit
9. exception ImportError
10.exception ModuleNotFoundError
11.exception IndexError
12.exception KeyError
13.exception KeyboardInterrupt
14.exception MemoryError
15.exception NameError
16.exception NotImplementedError
17.exception OSError
18.exception ValueError
19.exception ZeroDivisionError
20.exception EnvironmentError
21.exception IOError
22.exception WindowsError
23.exception FileExistsError
24.exception FileNotFoundError
25.exception NotADirectoryError   
"""
# try :
#      fetcher(x,7)
# except IndexError:
#     print("Got Exception")
# Write a program to try block except block
# try:
#     a = int(input("Enter first number : "))
#     b = int(input("Enter second number : "))
#     c = a/b
#     print("Divide : ",c)
# except ZeroDivisionError:
#     print("Second number should be greater than Zero")
# except ValueError:
#     print("Only numberic value allowed")
# except:
#     print("User end error")
"""
raise It is used to raise exception either user defined exception and pre-defined exception through coding.
Syntax-------
    try:
        raise pre-defined exception / user defined exception
    except pre-defined exception /user defined exception:
    ---How to create user defined exception
    1. first of all create new class derived from exception class
        example
        class AgeError (Exception):
            pass
        class BalanceError(Exception):
            pass
finally - Finaly block if we want to excute any statment compulsary then finally block is suggested. for example
file closing, database closing.
finaly block excuted in following cases:
1. Even there is exception
2. Even there is no exception
3. Even there is matching except
4. Even there is no matching except
Note : finally block should be implement after all except blocks 
Syntax- 
    try:
        -----------------
        -----------------
        -----------------
    except Exception object:
        ------------------
        ----------------
        -----------------
    finally:
        ------------------
        ------------------
        ------------------
"""
# class AgeError (Exception):
#     pass
# try:
#     id = int(input("Enter Emp id :"))
#     ename = input("Enter Emp name : ")
#     salary = float(input("Enter emp salary : "))
#     age= int(input("Enter emp age : "))
#     if age<20 or age>30:
#         raise AgeError()
#     print("Emp Id : ",id)
#     print("Emp Name : ",ename)
#     print("Emp age : ",age)
#     print("Emp salary : ",salary)
# except AgeError:
#     print("Employee must between 20 to 30 years")
# except ValueError:
#     print("Only numeric value is allowed")
# finaly block examples:
# def after():
#     try:
#         ch=fetcher(x,8)
#         print(ch)
#     except IndexError:
#         print("Invalid Index")
#     finally:
#         print("Finally Block")
# after()
# print("after try")
#Write a program to Complete Exception Handling in Python
class AgeError(Exception): pass
class BalanceError(Exception): pass
try:
    id = int(input("Enter Employee id :"))
    name = input("Enter Employee name :")
    age = int(input("Enter Employee age :"))
    salary = float(input("Enter Employee salary :"))
    if age<20 or age>30:
        raise AgeError()
    if salary<=2000.0:
        raise BalanceError()
    print("Employee ID :",id)
    print("Employee Name :",name)
    print("Employee Age :",age)
    print("Employee Salary :",salary)
except ValueError:
    print("Only number allowd try again")
except AgeError:
    print("Employee age between 20 to 30 years only")
except BalanceError:
    print("Employee salary should be 2000")
except Exception:
    print("Some things errors.")
finally:
    print("Thank you for visiting my apps")

