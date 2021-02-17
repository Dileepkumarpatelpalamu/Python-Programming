import copy
# rows= int(input("Enter no of rows of matrix :"))
# cols = int(input("Enter no of cols of matrix :"))
# matrix=[]
# for i in range(rows):
#     a = []
#     for j in range(cols):
#         x = int(input("Enter "+str(i+1)+" rows "+str(j+1)+" Element :"))
#         a.append(x)
#     matrix.append(a)
# print(matrix)
# print("Display Matrix :")
# for i in range(rows):
#     add =0
#     for j in range(cols):
#         add = add+matrix[i][j]
#         print(matrix[i][j],end=" ")
#     print()
# print("Transpose of matrix")
# for i in range(rows):
#     #add =0
#     for j in range(cols):
#         #add = add+matrix[i][j]
#         print(matrix[j][i],end=" ")
#     print()
# for i in range(rows):
#     add =0
#     for j in range(cols):
#         add = add+matrix[i][j]
#     print("rows :",(i+1)," Sum :",add)
# for i in range(rows):
#     add =0
#     for j in range(cols):
#         add = add+matrix[j][i]
#     print("cols :",(i+1)," Sum :",add)
#     mysum=0
# for i in range(rows):
#     for j in range(cols):
#         if i == j:
#             mysum = mysum+matrix[i][j]
# print("Sum of DIG is :",mysum)
#List Comprehension
x=[[1,2,3],[4,5,6],[7,8,9]]
#display list element using list comprehension
# y=[[x[i][j] for j in range(len(x))] for i in range(len(x))]
# print(y)
# Write a program to print transpose of element
# y=[[x[j][i] for j in range(len(x))] for i in range(len(x))]
# print(y)
# Write a program to print sum of each rows in list
# y=[sum(x[i]) for i in range(len(x))]
# print(y)
#Write a program to odd number using list comprehension
# y=[ i for i in range(1,50) if i%2==0]
# print("Even number :",y)
#Write a program to print odd number using list comprehension
# y=[ i for i in range(1,50) if i%2==1]
# print("Odd number :",y)
#Write a program to print given format
# """['*', 'e', '*', '*', 'o']"""
# l="hello"
# y=[ch if ch in "aeiou" else "*" for ch in l]
# print(y)
#list function in Revision 
#append()
#remove()
#pop()
#extend()
#count()
#insert()
#sort()
#sorted()
#append()--------------------
l=[200,50,5,4,8,2,4,6,7,8]
# l.append("Raju")
# print(l)
#remove()------This function is use to remove element of list
# l.remove(True)
# print(l)
# pop()------This function is use to remove element using index number by default index number is lenth of string
# l.pop()
# print(l)
# extend()-- This function is use to insert multipal elemet in list by default element is inserted in last 
# l.extend([10,50,"Maya","Rohit"])
# l.extend("Dileep")
# print(l)
# count()------This function is use to count itratable list item 
# m=l.count(8)
# print(m)
#insert(indexnumber,itemvalue)------ This function is use to insert element in list in specify index number
# l.insert(5,"Raja Saheb")
# print(l)
#sort()----- This funcion is used to accending or decending order
#l.sort() accending order
#l.sort(reverse=True) desencing order
#sorted() This function is used to accending order or decending order
# m = sorted(l,reverse=True)
# print(m)
#print(l)
#index()----this function is used to find index of element of list
#print(l.index(7))
#How to use list slicing
# l=[200,50,5,4,8,2,4,6,7,8,[10,50]]
# m=l.copy()
# m.append("52")
# print(l)
