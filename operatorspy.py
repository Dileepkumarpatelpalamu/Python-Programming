"""
Following Opetators in Python
1. Arthmetic operators
	1. Addition (+)
	2. Aubtraction (-)
	3. Multiplication (*)
	4. Division (/)
	5. Reminder (%)
	6. Floor Division (//)
	7. Exponent (**)
"""
#Example of arthmetic operators
# f1 = int(input("Enter first No : "))
# f2 = int(input("Enter second No : "))
# print("Sum of Num :",f1+f2)
# print("Subtraction of Num :",f1-f2)
# print("Multiplication of Num :",f1*f2)
# print("Division of Num :",f1/f2)
# print("Reminder of Num :",f1%f2)
# print("Floor Division of Num :",f1//f2)
# print("Power of Num :",f1**f2)
"""
2. Comparison operators
	1. Equality (==)
	2. Not equal (!=)
	3. Less than equal (<=)	
	4. Greater than equal (>=)
	5. Less than (<)
	6. Greater than (>)
"""
# Example of comparision operator
# f1 = int(input("Enter first No : "))
# f2 = int(input("Enter second No : "))
# print("Equality : ",f1 == f2)
# print("Not equal : ",f1 != f2)
# print("Less than equal : ",f1 <= f2)
# print("Greter than qual ",f1 >= f2)
# print("Less than : ",f1 < f2)
# print("Greater than ",f1 > f2)
"""
3. Assignment operators
	1. assignment (=)
	2. plus assignment (+=)
	3. minus assignment (-=)
	4. Mulplication assignment(*=)
	5. Reminder assignment(%=)
	6. Exponent assignment(**=)
	7. Floar assignment (//=)
"""
# Example of assignment operator
# f1 = int(input("Enter first No : "))
# r1=r2=r3=r4=r5=r6=r7=f1
# r1 +=5
# r2 -=5
# r3 *=5
# r4 /=5
# r5 %=5
# r6 **= 5
# r7 //=5
# print("Assignment : ",f1)
# print("Plus Assignment : ",r1)
# print("Minus Assignment : ",r2)
# print("Multiplication Assignment : ",r3)
# print("Division Assignment : ",r4)
# print("Reminder Assignment : ",r5)
# print("Exponent Assignment : ",r6)
# print("Floor Assignment : ",r7)
"""
4. Bitwise operators
	1. Binary and (&)
	2. Binary or (|)
	3. Binary xor (^)
	4. Negation (~)
	5. Left sift (<<)
	6. Right sift (>>)
"""
#example of Bitwise oprators
# f1 = int(input("Enter first No : "))
# f2 = int(input("Enter second No : "))
# #1010
# #1100
# print("Binary And :",f1 & f2)
# print("Binary Or :",f1 | f2)
# print("Binary Xor :",f1 ^ f2)
# print("Binary Negation :",~f2)
# print("Left Sift Value :",f1<<2)
# print("Right Sift value  :",f1>>2)
"""
5. Logical operators
	1. and
	2. or
	3. not
"""
# f1 = int(input("Enter first No : "))
# f2 = int(input("Enter second No : "))
# if f1 and f2 :
#     print("And Operator Satified")
# if f1 or f2 :
#     print("Or operator satified")
# if  not f2:
#     print("Not operator satisfied")
"""
6. Membership operators 
	1. in 
	2. not in
"""
# lst = ['Dileep','Mohan','Rohan','Mohini','Rakesh']
# for item in lst:
#     print(item, end =", ")
# print()
# for item in lst:
#     if "Dileep" not in item:
#         print(item, end =", ")
# print()
"""
7. Identity operators
	1. is 
	2. is not
"""
# f1=int(input("Enter first No : "))
# f2=int(input("Enter first No : "))
# print("IS Operator : ",f1 is f2)
# print("IS NOT Operator : ",f1 is not f2)
import sqlite3