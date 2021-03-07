import os as py
""""---------Most important os module function
1.os.name()
2. os.mkdir()
3. os.getcwd()
4. os.chdir()
5. os.rmdir()
6. os.error()
7. os.rename()
"""
# print("Operating System :",py.name)
# print("Create Directory :",py.mkdir('Student'))
# print("Working Directory :",py.getcwd())
#print("Change Direcory :",py.chdir('D:\\'))
# if py.rmdir('Student'):
#     print("Directory Deleted Sucessfully")
# else:
#     print("Directory not found")
# Write a program to find binary to decimal
# n = int(input("Enter Binary No : "))
# base,dec,sum = 1,0,0
# while n>0:
#     r= n%10;
#     dec = r * base  
#     sum = sum +dec
#     base = base*2
#     n= n//10  
# print("Decimal value : ",sum)
# Other way to find decimal value in python
# n = int(input("Enter Binary No : "))
# base, i,dec = 2,0,0
# while n >0: 
#     dec = dec + (n%10 * base ** i)
#     n = n//10
#     i+=1
# print("Decimal Value : ",dec)
# # Other way to evalue Binary to decimal
# n= int(input("Enter Binary number : "),2)
# print("Decimal Value : ",n)
#Write a program to convert Decimal to binary
# n = int(input("Enter Decimal number : "))
# binstr,base='',2
# while n>0:
#     r = n%base
#     binstr = binstr + str(r)
#     n = n//base
# print("Binary no : ",binstr[::-1])
# another way to conver Decimal value
# n = int(input("Enter decimal number :"))
# n=6
# strbin,base,val=0,2,1
# while n>0:
#     r = n % base
#     strbin =strbin + r * val
#     n = n//base
#     val*=10
# print("Binary No : ",strbin)
# another way convert Decimal to Binary
# n = bin(int(input("Enter Decimal no : "),10))
# print("Binary Number : ",n[2::])
