# Description: Given a string and a non-negative int n, return a larger string that is n copies of the original string.
# Author: John Royce Punay
# Date created: March 5, 2018 7:20 PM
# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'


# Solution 1
def string_times1(word, count):
    if count < 0:
        print("Oops! negative value is not accepted for duplacating the string.")
        return False
    else:
        return word.capitalize() * count


# Solution 2

def string_times2(str, n):
  result = ""
  for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
    result = result + str  # could use += here
  return result
