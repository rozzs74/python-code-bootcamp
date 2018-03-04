# Description:Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged. 
# Author: John Royce Punay
# Date created: March 4, 2018 7:53 PM
# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'


# Solution 1
def not_string1(word):
    word_split = word.split()
    if word_split[0] == "not":
        return word
    else:
        return f"not {word}"

# Solution 2
def not_string2(word):
    if len(word) >= 3 and word[:3] == 'not':
        return word
    return f"not {word}"

print(not_string2('notbad'))