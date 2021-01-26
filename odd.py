print("Enter outer limit of odd number :")
try:
    num = int(input())
    print(F"Odd number : {num} are ")
    for i in range(1,num + 1):
        if i % 2 == 1:
            print(i)
except:
    print("String could not be allowed")