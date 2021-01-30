a = int(input("enter first no :\n"))
b = int(input("enter second no :\n"))
c = int(input("enter third no : \n"))
d = int(input("enter forth no: \n"))
if a>b and a>c and a>d :
    print(a,"is the biggest no")
elif b>c and b>d :
    print(b, "is the begest no")
elif c>d:
    print(c,"is the biggest no")
else:
    print(d,"is the biggest no")