# Description: Program that asks for an integer and prints the square of it. Use a while loop with try,except,else block to account 
# for incorrect inputs
# Author: John Royce Punay
# Date created: March 11, 2018 8:37 AM


def ask():
    while True:
        try:
            number = int(input("Please enter number: "))
            number ** 2
        except ValueError:
            print("Invalid number")
            continue
        else:
            print(f"No errors here is the result {number}")
            break
        finally:
            print("Once done I am printing always")

ask()
