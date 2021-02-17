#Solution of test 2 organized on dated 13-jan-2021
# 3Remove dublicate value in list
# l=[1,2,3,2,1,3,4,5,2,3]
# m =[]
# for ch in l:
#     if ch not in m:
#         m.append(ch)
# print("Unique value in List :",m)
#op=[1,2,3,4,5]
#5 l=[[1,2,3],[3,4,5],[6,8,9]]
# print("lenth of list :",len(l))
#op=3
#6print(str([1,2])+"34")
#op=[1,2]34
#7 l =[1,2,3,4,5]
# l[1:3]=[10,15]
# print(l)
#op=[1,10,15,4,5]
#8 l=[1,6,7,4,5,3]
# l[1:2]=[]
# print(l)
#op=[1,7,4,5,3]
#9
# l=[1]
# l[:0]=[2,3,4]
# print(l)
#op=[2,3,4,1]
#10
# l=["Satya","Mohan","Praveen"]
# l2=l.sort()
# print(l2)
#op=None
#11
# l =['abc','abd','abe']
# l.sort(reverse=True)
# print(l)
#op =['abe','abd','abc']
#12
# x=[15,344.55,"Metier","Career","Solution"]
# a,*_,c,d=x
# print(c)
#op=Career
# x=["Metier","Career","Solution"]
# for val in x:
#     print(val,"length is :",len(val))
#     for v in val:
#         print(v)
#op=
#Metier length is :6
#M
#e
#t
#i
#e
#r
#Career length is :6
#C
#a
#r
#e
#e
#r
#Solution length is :8
#S
#o
#l
#u
#t
#i
#o
#n
# x=["Metier","Career","Solution"]
# for data in range(len(x)):
#     y = x[data]
#     for i in range(len(y)):
#         for j in range(0,i+1):
#             print(y[j],end="")
#         print()
#M
#Me
#Met
#Meti
#Metie
#Metier
#C
#Ca
#Car
#Care
#Caree
#Career
#S
#So
#Sol
#Solu
#Solut
#Soluti
#Solutio
#Solution
#x=[[1,2,3],[4,5,6],[7,8,9]]
# l =[[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
# print(l)
# op=[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# num = 10
# bin_num=bin(num)
# new_bin=bin_num[2:]
# print(new_bin)
#op=1010