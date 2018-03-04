# Description: Given two int values, return their sum. Unless the two values are the same, then return double their sum.
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
# Author: John Royce Punay
# Date created: March 4, 2018 1:03 PM
# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

def sum_double(*args):
    if args[0] == args[1]:
        return sum(args) * 2
    return sum(args)

print(sum_double(2,2))