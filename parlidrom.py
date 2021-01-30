num = int(input("enter any num : \n"))
origin = num
rev = 0
while num>0:
    r = num % 10
    rev = rev * 10 + r
    num = num // 10
if origin == rev :
    print("Input Number parlidrome")
else:
    print("Input Number not parlidrome")