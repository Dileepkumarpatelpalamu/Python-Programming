print("Enter outer limit of even number :")
try:
    num = int(input())
    print(F"Even number : {num} are ")
    for i in range(1,num + 1):
        if i % 2 == 0:
            print(i)
except:
    print("String could not be allowed")