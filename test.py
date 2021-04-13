#How to remove common item in both list
# str1 =list("SAMANTHA")
# str2 =list("NAGACHAITANYA")
# for ch in str1:
#     if ch in str2:
#         str1.remove(ch)
#         str2.remove(ch)
# str3 = str1+str2
# size = len(str3)
# print(size)
# str3 = list(str3)
# print(str3)
# while size>1:
#     if size>10:
#         r = 10
#         str3.pop(r-1)
#     else:
#         r = 10 % size
#         str3.pop(r-1)
#     size= len(str3)
# print(str3)
# logic to remove items of list postition at 10 but index 9
# lst = [1,2,3,4,5,6,7,8,9,10,11,12]
# size = len(lst)
# while size>1:
#     if size>10:
#         r = 10
#         lst.pop(r-1)
#     else:
#         r = 10 % size
#         lst.pop(r-1)
#     size= len(lst)
# print(lst)
name1 = list(input("Enter First Name : "))
name2 = list(input("Enter Last Name : "))
for ch in name1[:]:
    if ch in name2:
        name1.remove(ch)
        name2.remove(ch)
name3 = name1 + name2
print(name3)
for ch in name3:
    if ch=="":
        name3.remove(ch)
ln = len(name3)
flms = list("FLAMES")
cnt = 0
while(len(flms)>1):
    for i in range(len(flms)):
        cnt +=1
        if i == len(flms):
            break
        if cnt == ln-1:
            flms.pop(i)
            cnt = 0
flames =["Friends","Lovers","Affection","Marriage","Enemies","Siblings"]
for name in flames:
    if name.startswith(flms[0]):
        print("Relation between them",name)