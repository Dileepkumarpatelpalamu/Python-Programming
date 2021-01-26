print("Enter Starting Number: ")
start = int(input())
print("Enter Ending Number: ")
stop = int(input())
count = 0
print(f"Display all number between {start} and {stop}")
print("=================================================")
for i in range(start,stop+1):
    if i>1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)
            count += 1
print("==================================================")
print("Total No of Prime No is :" ,count)