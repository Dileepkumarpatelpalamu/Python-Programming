#find biggest no using turnay operator
f = int(input("Enter first no :\n"))
s = int(input("Enter second no : \n"))
t = int(input("Enter third no : \n"))
max = f if f>s and f>t else s if s>t else t
print("Max value is :",max)