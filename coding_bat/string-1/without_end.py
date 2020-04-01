# Given a string, return a version without the first and last char, so "Hello" yields "ell". 
# The string length will be at least 2.

# Author John Royce Punay
# Date Created: April 1, 2020 7:13PM

# without_end('Hello') → 'ell'
# without_end('java') → 'av'
# without_end('coding') → 'odin'

def without_end(word):
	word_length = len(word)
	exclude_length = word_length - 1
	return word[1:exclude_length]
a = without_end("java")

print(a)