# Write a program to print no of days in months
months_days=[31,0,31,30,31,30,31,31,30,31,30,31]
yr=int(input("Enter year : "))
if((yr%4==0 and yr%100!=0) or yr%400==0):
	months_days[1]=29
else:
	months_days[1]=28
sums=[]
month=int(input("Enter month number : "))
for i in range(1,months_days[month-1]+1):
	sums.append(i)
print(sums)