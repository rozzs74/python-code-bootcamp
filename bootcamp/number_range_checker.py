# Description: Program that checks if a given number whether a number is in given range based on inclusive high and low number values
# Author: John Royce Punay
# Date created: March 3, 2018 9:44 PM


def number_range_checker(**kwargs):
    if kwargs['a'] in range(kwargs['b'], kwargs['c'] + 1):
        print(f"{kwargs['a']} is in the range between {kwargs['b']} and {kwargs['c']}")
    else:
        print("The number is outside range")

def main():
    print("<----- Number range checker---->")
    
    for i in  range(0, 3):
       try:
            first_number = int(input("Please enter number: "))
            lower_range_number = int(input("Please enter lower range number: "))
            higher_range_number = int(input("Please enter higher range numebr: "))
            number_range_checker(a=first_number, b=lower_range_number, c=higher_range_number)
            break
       except:
            ValueError
            print('Invalid input please enter number again!')
            continue    
    

main()



