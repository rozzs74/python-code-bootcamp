# Description: Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
# The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive)..
# Author: John Royce Punay
# Date created: March 4, 2018 8:01 PM
# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'

# Solution 1
def missing_char1(word, index):
    word_list = list(word)
    if index > len(word_list):
        return f"Oops index range error"
    else:
        word_list.pop(index)
        return "".join(word_list)
# Solution 2
print(missing_char1('kitten', 5))

def missing_char2(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back
print(missing_char2('kitten', 5))