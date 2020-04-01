# Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" 
# yields the empty string "". 

# Author: John Royce Punay
# Date created: April 1, 2020 5:22 PM

# first_two('Hello') → 'He'
# first_two('abcdefg') → 'ab'
# first_two('ab') → 'ab'

def first_two(word):
	word_length = len(word)
	if(word_length < 2):
		return word
	else:
		return word[0:2]

a = first_two("abcedf")
print(a)