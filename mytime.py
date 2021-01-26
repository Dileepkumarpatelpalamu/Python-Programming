# How to use time module 
import time
starttime = time.time()
for i in range(45):
	print("Welcome to Python")
	time.sleep(1)
print("The while loop executed in seconds :", time.time()-starttime)
starttime2 = time.time()
i = 0
while(i<45):
	print("Welcome to Python")
	i +=1
print("The for loop executed in seconds :", time.time()-starttime2)
