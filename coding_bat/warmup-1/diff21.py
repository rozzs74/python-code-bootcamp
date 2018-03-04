# Description: Given an int n, return the absolute difference between n and 21, 
# except return double the absolute difference if n is over 21.
# Author: John Royce Punay
# Date created: March 4, 2018 1:10 PM
# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0



def diff21(number):
    difference = abs(21 - number)
    if number > 21:
        difference *2
    return difference
print(diff21(21))