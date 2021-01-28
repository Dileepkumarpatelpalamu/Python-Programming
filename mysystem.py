import sys as system
while True:
    print("Enter the any string or number")
    data = input()
    print(f"Size of Input string or number :{system.getsizeof(data)} and Address : {id(data)}")
    if data == "q":
        print("Thank you for visiting operation")
        break
