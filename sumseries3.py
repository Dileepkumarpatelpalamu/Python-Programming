num = int(input("enter any number :"))
mysum = 0
print("Sum of prime no is :")
for i in range(2,num+1):
    for j in range(2,(i//2)+1):
        if i % j == 0:
            break
    else:
        mysum = mysum + i
        print(f"{i} +",end=" ")
print("=",mysum)
