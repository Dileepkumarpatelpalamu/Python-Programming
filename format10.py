""" Write the program print given format
123454321
 1234321
  12321
   121
    1
"""
rows = int(input("enter no of rows :"))
for i in range(1,rows+1):
    for n in range(0,i-1):
        print(end=" ")
    for o in range(1,rows-i+1):
        print(o, end="")
    for p in range(rows-i-1,0,-1):
        print(p,end="")
    print()