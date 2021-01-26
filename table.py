print("Enter the number that is used to Print Table : ")
try:
    num = int(input())
    print(F"Table of number : {num} are ")
    for i in range(1,11):
        print(f"{i} * {num} =", i * num)
except:
    print("String could not be allowed")