# write a program to print prime number
num = int(input("Enter any number :"))
primes = [i for i in range(2, num + 1) if all(i%j != 0 for j in range(2, int(i ** 0.5) + 1))]
print("Total Prime No is :",primes," Total No of Prime No is :",str(len(primes)))


