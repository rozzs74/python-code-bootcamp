"""
Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence 
to that number or to the Nth number.
"""


def enter_number():
	"""
	Function definition for accepting input number of user
	"""
	while True:
		try:
			number = int(input("Please enter number for fibonnaci length sequence: "))
		except ValueError:
			print("Please enter valid number")
			continue
		else:
			return generate_fibonacci_sequence(number)


def generate_fibonacci_sequence(number):
	"""
	Function definition for generating fibonnaci sequence
	"""
	fibonacci_sequence = [0]
	while len(fibonacci_sequence) < number:
		if len(fibonacci_sequence) == 1:
			fibonacci_sequence.append(1)
		else:
			fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
			
	return f"Your Fibonacci sequence are: {collect_fibonnaci(fibonacci_sequence)}"

def collect_fibonnaci(sequence):

	for number in range(len(sequence)):
		sequence[number] = str(sequence[number])
	return ", ".join(sequence)
		
def main():
	print(enter_number())

if __name__ == '__main__': # Runnin the python file
	main()
