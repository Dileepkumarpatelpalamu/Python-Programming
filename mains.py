import math as m
while True:
    print("""
            Mathematical Operation for Multiple form choose your choice:
            1. Power
            2. Square roots
            3. Exit The program
            Enter Your Choice :
     """)
    choice = input()
    if choice == "3":
        break
    elif int(choice)==1:
        print("Enter the base value :")
        base = int(input())
        print("Enter the Power value :")
        power = int(input())
        print("power value of entered number :",pow(base,power))
    elif int(choice)==2:
        print("Enter the number to find square roots :")
        num = int(input())
        print("Square roots of entered number :",m.sqrt(num))


     


