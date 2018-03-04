# Description: Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10.
# Author: John Royce Punay
# Date created: March 4, 2018 7:13 PM
# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True

def makes10(x, y):
    return (x == 10 or y == 10) or ((x + y) == 10)

print(makes10(1, 9))