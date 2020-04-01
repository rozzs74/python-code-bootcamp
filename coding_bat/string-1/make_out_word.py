# Given an "out" string length 4, such as "<<>>", and a word, 
# return a new string where the word is in the middle of the out string, e.g. "<<word>>". 

# Author: John Royce Punay
# Date created: March 31, 2020 6:44 PM

# make_out_word('<<>>', 'Yay') → '<<Yay>>'
# make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
# make_out_word('[[]]', 'word') → '[[word]]'

def make_out_word1(delimeter, word):
	delimeter_length = len(delimeter)
	if(delimeter_length != 4):
		raise ValueError("Invalid delimeter length")
	else:
		start = delimeter[:2]
		end = delimeter[2:4]
		return "{}{}{}".format(start, word,end)
a = make_out_word1("<<??", "rouyce")

print(a)