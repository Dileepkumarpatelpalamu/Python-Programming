while True:
	print("--------------------------------------------------------------------------")
	print("Computer based numbers convetion")
	print("""
			1. Decimal To Binary
			2. Decimal To Octal
			3. Decimal To Hexadecimal
			4. Octal To Binary
			5. Octal To Decimal
			6. Octal To Hexadecimal
			7. Binary To Decimal
			8. Binary To Octal
			9. Binary To Hexadecimal
			10. Hexadecimal To Decimal
			11. Hexadecimal To Octal
			12. Hexadecimal To Binary
			13. Exit The Conversion System
		""")
	print("--------------------------------------------------------------------------")
	print("Enter your Choice:")
	choice = int(input())
	print("--------------------------------------------------------------------------")
	if choice == 13:
		print("Thank You for visiting Convertion System")
		print("--------------------------------------------------------------------------")
		break
	elif choice == 1:
		print("Enter any Decimal Number:")
		dec_num = int(input())
		print(f"The {dec_num1} is equal binary number : {bin(dec_num)}")
	elif choice == 2:
		print("Enter any Decimal Number:")
		dec_num = int(input())
		print(f"The {dec_num} is equal Octal number : {oct(dec_num)}")
	elif choice == 3:
		print("Enter any Decimal Number:")
		dec_num = int(input())
		print(f"The {dec_num} is equal hexadecimal number : {hex(dec_num)}")
	elif choice == 4:
		print("Enter any Octal Number:")
		dec_num = input()
		dec_bin = int(dec_num,8)
		print(f"The {dec_num} is equal binary number : {bin(dec_bin)}")
	elif choice == 5:
		print("Enter any Octal Number:")
		dec_num = input()
		dec_bin = int(dec_num,8)
		print(f"The {dec_num} is equal Decimal number : {dec_bin}")
	elif choice == 6:
		print("Enter any Octal Number:")
		dec_num = input()
		dec_bin = int(dec_num,8)
		print(f"The {dec_num} is equal Decimal number : {hex(dec_bin)}")
	elif choice == 7:
		print("Enter any Binary Number:")
		dec_num = input()
		dec_bin = int(dec_num,2)
		print(f"The {dec_num} is equal Decimal number : {dec_bin}")
	elif choice == 8:
		print("Enter any Binary Number:")
		dec_num = input()
		dec_bin = int(dec_num,2)
		print(f"The {dec_num} is equal Octal number : {oct(dec_bin)}")
	elif choice == 9:
		print("Enter any Binary Number:")
		dec_num = input()
		dec_bin = int(dec_num,2)
		print(f"The {dec_num} is equal Hexadecimal number : {hex(dec_bin)}")
	elif choice == 10:
		print("Enter any hexadecimal Number:")
		dec_num = input()
		dec_bin = int(dec_num,16)
		print(f"The {dec_num} is equal decimal number : {dec_bin}")
	elif choice == 11:
		print("Enter any hexadecimal Number:")
		dec_num = input()
		dec_bin = int(dec_num,16)
		print(f"The {dec_num} is equal Octal number : {oct(dec_bin)}")
	elif choice == 12:
		print("Enter any hexadecimal Number:")
		dec_num = input()
		dec_bin = int(dec_num,16)
		print(f"The {dec_num} is equal Binary number : {bin(dec_bin)}")
	else:
		print("Please Enter Valid choice")
		print("--------------------------------------------------------------------------")
	print("--------------------------------------------------------------------------")
