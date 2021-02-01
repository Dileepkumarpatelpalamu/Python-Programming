#Write a program for print all factor of input number
num = int(input("Enter any number :"))
print("Factor of",num, "are :")
for i in range(1,num+1):
    if(num % i == 0):
        print(i)