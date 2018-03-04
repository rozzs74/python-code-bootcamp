# Description: Program that checks if the string is pangram or not
# Author: John Royce Punay
# Date created: March 3, 2018 11:55 AM


from string import ascii_lowercase

def is_pangram(word):
    alphaset = set(ascii_lowercase)
    return alphaset <= set(word.lower())  

print(is_pangram("The quick brown fox jumps over the lazy dog"))