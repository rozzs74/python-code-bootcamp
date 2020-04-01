# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. 
# The string length will be at least 2.
#Author: John Royce Punay

#Date created: April 1, 2020 7:33AM

# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'

def left2(word):
	word_length = len(word)
	return word[2:word_length] + word[0:2] if word_length > 2 else word



a = left2("java")
print(a)