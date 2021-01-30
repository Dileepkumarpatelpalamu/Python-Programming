import math as m
while True:
    print("---------------------------------------------------------------------------------")
    print("1. Areas\n2. Perimiter\n3. Exit\n")
    print("----------------------------------------------------------------------------------")
    ch = int(input("Enter Your Choice :"))
    print("----------------------------------------------------------------------------------")
    if ch == 1:
        while True:
            print("----------------------------------------------------------------------------------")
            print("You can choose required figure for area :")
            print("1. Circle\n2. Square\n3. Rectangle\n4. Tringle\n5. Parallel\n")
            print("----------------------------------------------------------------------------------")
            choice = int(input("Enter area figure serial No :"))
            if choice == 1:
                radius = float(input("Enter the circle radius : "))
                print("Area of the circle is :",3.14*radius**2)
            elif choice == 2:
                side = float(input("Enter the side of square : "))
                print("Area of the square is :",side**2)
            elif choice == 3:
                l = float(input("Enter lenth of rectangel : "))
                b = float(input("Enter breath of rectangel : "))
                print("Area of the circle is :",l*b)
            elif choice == 4:

            else:
                print("Thank you for visiting")
                break
    elif ch == 2:
        print("----------------------------------------------------------------------------------")
        print("You can choose required figure for perimiter :")
        print("1. Circle\n2. Square\n3. Rectangle\n4. Tringle\n5. Parallel\n")
        print("----------------------------------------------------------------------------------")
    elif ch == 3:
        print("----------------------------------------------------------------------------------")
        print("Thank you for visiting for calculation")
        print("----------------------------------------------------------------------------------")
        break
    else:
        print("Please Enter Valid option")
