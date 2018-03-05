# Description: We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
# Author: John Royce Punay
# Date created: March 4, 2018 12:31 PM
# T, T ==> T
# F, F ==> T
# T, F ==> F 

def monkey_trouble(a_smile, b_smile):
    return ((a_smile and b_smile) or (not a_smile and not b_smile))

print(monkey_trouble(True, False))