# Display tuple item using loop
lst1 =(12,14,16,18,20,20)
print("Tuple items are :", end="\t")
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
