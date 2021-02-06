# Operator	Description
# +	It is known as concatenation operator used to join the strings given either side of the operator.
# *	It is known as repetition operator. It concatenates the multiple copies of the same string.
# [:]	It is known as range slice operator. It is used to access the characters from the specified range.
# in	It is known as membership operator. It returns if a particular sub-string is present in the specified string.
# not in	It is also a membership operator and does the exact reverse of in. It returns true if a particular substring is not present in the specified string.#r/R	It is used to specify the raw string. Raw strings are used in the cases where we need to print the actual meaning of escape characters such as "C://python". To define any string as a raw string, the character r or R is followed by the string.
# %	It is used to perform string formatting. It makes use of the format specifiers used in C programming like %d or %f to map their values in python. We will discuss how formatting is done in python.
#string1 = input("Entry first string :")
#string2 = input("enter second string")
# + operator is used to add to string1 and string2 as well as also add number
#print("Main string :", string1 + string2)
#print ("Sum of No :",50+20)
# * operator is used to reapeted of string
#mystring = string1 *5
# [startindex:endindex:stepvalue] is also know as slicing operator in python
# [0:lenth of string:1]
# for mystring in string1:
#     print(mystring)
# if "d" not in string1:
#     print("not found")
# num = 12
# myfloat = 18.90
# mystr   = "I like python"
# using % symbols usig string format
# print("Number :%d Float : %f Mystring : %s"%(num,myfloat,mystr))
# using format string
# print("{} and {} are the best friends".format("Rohit","Virat"))
# f string usng string format string
# virat = "Virat"
# rohit = "Rohit"
# print(f"{virat} and {rohit} are the best friends")
#Espace Sequence		Description
# 1. \newline		It ignores the new line
# 2. \\			Backslash
# 3. \'			Single Quotes
# 4. \\"			Double Quots
# 5. \a			ASCII Bell
# 6. \b			ASCII Backspace
# 7. \f			ASCII Formfeed
# 8. \n			ASCII Linefeed
# 9. \r			ASCII Carriege Return
# 10. \t			ASCII Horizontal Tab
# 11. \v			ASCII Vertical Tab
# mystr = ["\\newlineDileep","\\Dileep","\Dileep'",'\\Dileep',"\aDileep","\bDileep","\fDileep","\nDileep","\rDileep","\tDileep","\vDileep"]
# for item in mystr:
#     print(item)



# user_name = input("Enter user name :")
# if len(user_name)>=8 and user_name.isalpha():
#     user_pass = input("Enter password:")
#     if len(user_pass)>=8 and user_pass.isalpha():
#         if user_name == 'dileepkumarpatel' and user_pass == 'DTGpalamu':
#             print(" your credential are match : You can login")
#         else:
#             print("Invalid user and password: Try again!!!!!")
#     else:
#         print("Invalid password :  must have  8 or greater than 8 alphabet character")
# else:
#     print("Invalid user name : user must 8 or greater than 8 alphabet character")
