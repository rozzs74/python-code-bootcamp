# Description: Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
#  Return n copies of the front;
# Author: John Royce Punay
# Date created: March 5, 2018 7:43 PM
# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'


# Solution 1
def string_bits1(word):
    letters = list(word)
    result = []
    for index in range(len(letters)):
        if index % 2 == 0:
            result.append(letters[index])
    return "".join(result)

print(string_bits1("Hello"))


# Solution 2
def string_bits2(str):
  result = ""
  # Many ways to do this. This uses the standard loop of i on every char,
  # and inside the loop skips the odd index values.
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
