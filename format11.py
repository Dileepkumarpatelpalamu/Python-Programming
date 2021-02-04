rows =int(input("Enter no of rows :"))
for i in range(1,rows+1):
    for k in range(1,rows-i+1):
        print(end=" ")
    for j in range(1,i+1):
        print(j,end="")
    for m in range(i-1,0,-1):
        print(m,end="")
    print()
for i in range(1,rows+1):
    for n in range(0,i):
        print(end=" ")
    for o in range(1,rows-i+1):
        print(o, end="")
    for p in range(rows-i-1,0,-1):
        print(p,end="")
    print()
