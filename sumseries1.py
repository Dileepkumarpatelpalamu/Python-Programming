#Write a program to print sum of even no
num = int(input("Enter any number :"))
mysum = 0
print("Sum of even no  :")
for i in range(1,num+1):
    if i%2 == 0:
        if i == num :
            mysum = mysum +i
            print(i,"=",mysum)
        else:
            mysum = mysum + i
            print(i,"+",end=" ")