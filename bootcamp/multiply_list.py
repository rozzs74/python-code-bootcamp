# Description: Program that multiply items in list
# Author: John Royce Punay
# Date created: March 3, 2018 11:39 AM

mylist = [1, 2, 3, -5]


def multiply_list(lists):
	total = 1
	for item in lists:
		total *= item
	return total


print(multiply_list(mylist))