import random

secret_number = random.randint(1,20)
print('Guess number please!')
print('Heads up you have 7 times to guess the number think it in right way!')

for choice in range(7):
    chance = 6 - choice
    try:
        choice_number = int(input())    
        print("You have {} chance to guess a number".format(chance))        
        if choice_number < secret_number:
            print("You're selected number is too low")
        elif choice_number > secret_number:
            print("You're selected number is too high")
        else:
            print("Greate you get it!")
            break
    except:
        ValueError
        print("Invalid input please enter number")
        print("You have {} chance to guess a number".format(chance))        
        
if choice_number == secret_number:
    print("Yay it's correct your guess number is {} and the secret number is {}".format(choice_number, secret_number))


