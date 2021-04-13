name = input("Enter Your Name : ").lower().split()
mystr = ""
cur = 5
for name in name:
    mystr = mystr+name
nodublicate =""
for ch in mystr:
    if ch not in nodublicate:
        nodublicate = nodublicate + ch
nodublicate = list(nodublicate)
count= len(nodublicate)
while count>1:
    if count>10:
        i = 10
        nodublicate.pop(i-1)
    else:
        i = cur % count
        nodublicate.pop(i-1)
    count= len(nodublicate)
print(f"Entered name :{mystr} and Count : {cur} : ",nodublicate[0])

# name1 = list(input("Enter First Name :").lower())
# name2 = list(input("Enter Second Name :").lower())
# for ch in name1[:]:
#     if ch in name2:
#         name1.remove(ch)
#         name2.remove(ch)
# name3 = name1 + name2
# count= len(name3) # lenth of string after removing common letter in both string
# lst = ["Friends","Lovers","Marrage","Affectionate","Enemies","Simbling"]
# cur_count = 0 # variable is count for  current position
# i = 0   ## variable for indexing in lst
# while(len(lst)>1):
#     if cur_count == count-1: 
#         lst.pop(i)
#         cur_count=0
#     i = (i+1) % len(lst) # logic for increasing index for example above lst lenth is 6 then i = (0+1) % 6 that means  i =1 if i= 5 then exp result is i = 0 continue until while loop condition statisfied
#     cur_count +=1
# print("Relation Between Both :",lst[0])

