data ={"A":"Apple","B":"Ball", "C":"Cat", "D":"Doll","E":"Elephant"}
while True:
    print("Enter The Any Characters: exit to press q or Q ")
    print("================================================")
    char = input()
    if char == "q" or char == "Q":
        print("===========================================")
        print("Thank you for visiting the Dictionary")
        print("=============================================")
        break
    for key,item in data.items():
        if key == char.upper():
            print("=======================================")
            print(data[key])
            print("========================================")

        