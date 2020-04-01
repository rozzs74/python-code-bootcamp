# Description: Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
# Author: John Royce C. Punay
# Date created: March 29, 2020 9:40 AM
# Don't use for loops
# Sample execution
# make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'
 

# Solution 1
def make_abba(separator, word):
	return separator + word + word + separator

a = make_abba('Hi', 'Bye')
b = make_abba('Yo', 'Alice')
c = make_abba('What', 'Up')

print(f"Solution 1 output: {a}")
print(f"Solution 1 output: {b}")
print(f"Solution 1 output: {c}")

# Solution 2
def make_abba2(separator, word):
	prefix = separator * 1
	middle = prefix + (word[:] * 2) + prefix
	return middle

a = make_abba2('Hi', 'Bye')
b = make_abba2('Yo', 'Alice')
c = make_abba2('What', 'Up')

print(f"Solution 2 output: {a}")
print(f"Solution 2 output: {b}")
print("Solution 2 output {}".format(c * 2))