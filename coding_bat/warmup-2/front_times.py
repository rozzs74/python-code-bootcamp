# Description: Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3.
#  Return n copies of the front;
# Author: John Royce Punay
# Date created: March 5, 2018 7:32 PM
# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'


# Solution 1
def front_times1(word, count):
    front_word = word[:3]
    if count < 0:
        print(
            "Oops! negative value is not accepted for duplacating the string.")
        return False
    else:
        if len(word) < 3:
            return front_word * count
        else:
            return front_word * count


print(front_times1("abc", 3))

# Solution2
def front_times2(str, n):
    front_len = 3
    if front_len > len(str):
        front_len = len(str)
    front = str[:front_len]

    result = ""
    for i in range(n):
        result = result + front
    return result
