from random import randint

secret_number = randint(1,100)
print("WELCOME TO THE GUESS ME GAME CHALLENGE!")
print("Instructions!!!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
number_of_guess = []
guess_number = None
print("Secret {}".format(secret_number))

while secret_number != guess_number:
	try:
		 guess_number = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
		
		 # Check if out of bounds 
		 if (guess_number  < 1) or (guess_number > 100):
				print("OUT OF BOUNDS! Please try again")
				continue
		 else:
				number_of_guess.append(guess_number) # Append the guess number into list
				if len(number_of_guess) == 1:
					if abs(secret_number-guess_number) <= 10:
						print("WARM")
					else:
						print("COLD")
				else:
					previous_guess_number = number_of_guess[-2]

					if abs(secret_number - guess_number) < abs(secret_number - previous_guess_number):
						print("WARMER!")
					else: 
						print("COLDER!")
					 
					if guess_number == secret_number:
						print("You've guess it correctly!")
						print("It look {} times to guess the correct answer".format(len(number_of_guess)))
						break
	except:
		ValueError
		print("Invalid input please enter number")
		