# Write a program to sum of n mumber in python
num = int(input("Enter any number to dispaly series and sum :"))
mysum = 0
for i in range(1,num+1):
    if i == num:
        mysum = mysum + i
        print(i,"=",mysum)
    else:
        print(i,"+", end=" ")
        mysum = mysum + i