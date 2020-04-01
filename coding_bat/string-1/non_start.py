# Given 2 strings, return their concatenation, except omit the first char of each. 
# The strings will be at least length 1.

# non_start('Hello', 'There') → 'ellohere'
# non_start('java', 'code') → 'avaode'
# non_start('shotl', 'java') → 'hotlava'


def non_start(first_word, second_word):
	return first_word[1:len(first_word)] + second_word[1:len(second_word)] 

a = non_start("shotl", "java")
print(a)