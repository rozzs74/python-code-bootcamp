

# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

# Author: John Royce Punay
# Date created: April 1, 2020 5:30 PM

# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc'

def first_half(word):
	word_length = len(word)
	half_word_length = int(word_length / 2)
	return word[0:half_word_length]

a = first_half("WooHoo")

print(a)