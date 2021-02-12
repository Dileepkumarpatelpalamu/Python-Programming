string =input("Enter any string :")
print("String lenth increasing by one :")
for i in range(0,len(string)):
    for j in range(0,i+1):
        print(string[j],end="")
    print()
#print("String lenth decrease by one :")
for i in range(0,len(string)-1):
    for j in range(0,len(string)-i-1):
        print(string[j],end="")
    print()