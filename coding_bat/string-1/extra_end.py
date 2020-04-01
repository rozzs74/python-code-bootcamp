
#Given a string, return a new string made of 3 copies of the last 2 chars of the original string. 
# The string length will be at least 2.

# Author: John Royce Punay
# Date created: March 31, 2020 10:30 PM

# extra_end('Hello') → 'lololo'
# extra_end('ab') → 'ababab'
# extra_end('Hi') → 'HiHiHi'

def extra_end(word):
	word_length = len(word)
	if(word_length < 2):
		raise ValueError("Input should be greater than or equal to 2")
	return (word[-2] + word[-1]) * 3

a = extra_end("royce")
print(a)