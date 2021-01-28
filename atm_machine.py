total_amount = 0
def balance_enquiry(accountno):
	global total_amount
	return f"Total balance : {total_amount}"
def balance_deposit(accountno,amount):
	global total_amount
	total_amount= total_amount + amount
	return f"Total balance : {total_amount}"
def withdraw_blance(accountno,amount):
	global total_amount
	if total_amount < amount:
		return "Account No has been not succiffient blance"
	else:
		total_amount = total_amount - amount
		return f"Total amount is {total_amount}"
while True:
	print("============================================")
	print("Welcome Canera Bank to Payment System:")
	print("============================================")
	print("Now ! day following services are aviable")
	print("""
			1. Balance Enquery
			2. Deposite Amount
			3. Widthdraw Amount
			4. Exit 
			""")
	print("============================================")
	print("Enter your choice")
	choice = int(input())
	if choice == 4:
		print("============================================")
		print("Thank your for visiting Canera Bank")
		break
	elif choice == 1:
		print("Enter your Acount No:")
		account = input()
		enq_balance =balance_enquiry(account)
		print(enq_balance)
		print("============================================")
	elif choice == 2:
		print("Enter your Acount No:")
		dep_account = input()
		print("Enter amount :")
		dep_amount = int(input())
		dep_out = balance_deposit(dep_account,dep_amount)
		print(dep_out)
		print("============================================")
	elif choice == 3:
		print("Enter your Acount No:")
		wid_account = input()
		print("Enter amount :")
		wid_amount = int(input())
		wid_out = withdraw_blance(wid_account,wid_amount)
		print(wid_out)
		print("============================================")
	else:
		print("Please enter valid crentials")
	print("============================================")

