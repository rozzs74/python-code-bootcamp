"""
	Project Name: Find PI to the Nth Digit
	Instruction: Enter a number and have the program generate pi
				up to that many decimal places. Keep a limit to how far the program will go.
	Author: John Royce Punay
	Date created: March 12, 2018
"""
# First 1000 of digits for Pi value

pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

def find_pi_decimal():
	while True:
		try:
			decimal_place = int(input("Please enter nth digit for Pi: "))
		except ValueError:
			print("Invalid value")
			continue
		else:
			print(decimal_place)
			for index in range(0, len(pi)):
				print(pi[decimal_place:])
			break
		finally:
			print("Final block")

find_pi_decimal()

