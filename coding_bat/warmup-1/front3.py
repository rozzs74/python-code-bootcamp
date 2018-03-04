# Description: Given a string, we'll say that the front is the first 3 chars of the string. 
# If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
# Author: John Royce Punay
# Date created: March 4, 2018 8:14 PM
# front3('Java') → 'JavJavJav'
# front3('Chocolate') → 'ChoChoCho'
# front3('abc') → 'abcabcabc'

# Solution 1
def front31(word):
    if len(word) < 3:
        return word
    return word[:3] * 3

print(front31("ab"))

# Solution2 
def front32(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front )