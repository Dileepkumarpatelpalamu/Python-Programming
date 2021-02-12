#Write a program to print sum of odd no
num = int(input("Enter any number :"))
mysum = 0
print("Sum of odd no  :")
for i in range(1,num+1):
    if i%2 == 1:
        if i == num-1 :
            mysum = mysum +i
            print(i,"=",mysum)
        else:
            mysum = mysum + i
            print(i,"+",end=" ")