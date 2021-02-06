# Display list item using loop
lst1 =[12,14,16,18,20,20]
print("Array items are :", end="\t")
for item in lst1:
    print(item,end=" ")
print()
print("Positive index: ",end="\t")
for item in range(len(lst1)):
    print(item,end="  ")
print()
print("Negative Index :",end="\t")
for item in range(len(lst1),0,-1):
    print(item,end="  ")
print()
# List item slicing 
#print(lst1[-3:-4:-1])
#print(lst1[::-1])
#print(lst1[::])
#updating list element using index number
# lst1[0]=50
# lst1[4] = 30
# lst1[1:3]= "ram","Mohan","Sita"
# Operation perform on list
# 1. Repetition     The repetition operator enables the list elements to be repeated multiple times   
# 2. Concatenation	It concatenates the list mentioned on either side of the operator.
# 3. Membership	It returns true if a particular item exists in a particular list otherwise false.
# 4. Iteration	The for loop is used to iterate over the list elements.
# 5. Length	It is used to get the length of the list
#print(lst1 * 4)
#lst2 = [10,20,30,40,50,60]
#print(lst1+l)
#print(20 in lst1)
# for item in lst1:
#     print(item)
#print(len(lst1))
# adding the list element
# lst1.append(60)
# lst1.append(80)
# print(lst1)
# Remove the list element
#lst1.remove(20)
#print(lst1)

# In python many builtin function for list
# 1. len(list)	It is used to calculate the length of the list.
# 2. max(list)	It returns the maximum element of the list.
# 3. min(list)	It returns the minimum element of the list.
# 4. list(seq)	It converts any sequence to the list
#print(len(lst1))
#print(max(lst1))
#print(min(lst1))
#print(type(list(lst1)))
#multiple item input using list
# num = int(input("Enter no of element of list :"))
# for i in range(num):
#     lst1.append(int(input("Enter elemen of list :")))
# print(lst1)


