print("=========================================================================")
print("WELCOME TO PATEL INFOTECH SOLUTION DEVELOPED PERSONAL USE")
print("=========================================================================")

mysum = 0
while True:
	print("Select Your Choice")
	print("""
		1 == Addition
		2 == Subtraction
		3 == Multiplication
		4 == Division
		5 == Exit
		================================================================================
		""")
	print("Enter Your Choice")
	try:
		operations = int(input())
		if operations == 1:
			print("=================================================================================")
			print("Enter any number to Sum")
			myinput = int(input())
			mysum = mysum + myinput
			print(f"Total Weight/Gram/Meters/Number : {mysum}")
			print("=================================================================================")
		elif operations == 2 :
			print("=================================================================================")
			print("Enter any number to Subtract")
			myinput = int(input())
			mysum = mysum - myinput
			print(f"Total Weight/Gram/Meters/Number : {mysum}")
			print("=================================================================================")
		elif operations == 3 :
			print("=================================================================================")
			print("Enter any number to Multiply")
			myinput = int(input())
			mysum = mysum * myinput
			print(f"Total Weight/Gram/Meters/Number : {mysum}")
			print("=================================================================================")
		elif operations == 4 :
			print("=================================================================================")
			print("Enter any number to Divide")
			myinput = int(input())
			mysum = mysum / myinput
			print(f"Total Weight/Gram/Meters/Number : {mysum}")
			print("=================================================================================")	
		elif operations == 5:
			print("=================================================================================")
			print(f"Total Weight/Gram/Meters/Number : {mysum}")
			print("Thank you for visit the mycalc exit you")
			print("=================================================================================")
			break
	except:
		print("=================================================================================")
		print("Please Entered valid Choice")
		print("=================================================================================")
