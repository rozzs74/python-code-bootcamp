# Description: Given a non-empty string like "Code" return a string like "CCoCodCode".
#  Return n copies of the front;
# Author: John Royce Punay
# Date created: March 6, 2018 7:15 PM
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'


# Solution 1
def string_splosion(word):
    word_length = len(word)
    result = ""
    for i in range(word_length):
        result = result + word[:i+1]
    return result




print(string_splosion("Royce"))