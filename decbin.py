#How convert dec to binary using customize in python
num = int(input("enter any number :"))
def dectobin(num):
    if num>1:
        dectobin(num//2)
    print(num%2,end=" ")
def dectooct(num):
    if num >7:
        dectooct(num//8)
    print(num%8,end=" ")
print(num,"equal octal no is :")
dectooct(num)
#dectobin(num)
print()
