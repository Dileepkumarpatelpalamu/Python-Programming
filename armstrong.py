# Write a program to print input number is armstrong or not
num = input("Enter any number :")
m = int(num)
sum = 0
while(m>0):
    r = m % 10
    sum = sum + r ** len(num)
    m = m // 10
if (sum == int(num)):
    print("Input Number is armstrong")
else :
    print("Input number is not armstrong")