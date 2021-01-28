import keyword as key
print("Display all keyword in python")
mykey = key.kwlist
count = 0
print("Total No of Keywords :",len(mykey))
for item in mykey:
    count += 1
    print(f"{count} \t {item}")
    