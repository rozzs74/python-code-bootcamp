# Description: Program that checks if the string is palindrome or not
# Author: John Royce Punay
# Date created: March 3, 2018 11:55 AM


def palindrome(word):
    text = word.replace(" ", "")
    return text == text[::-1]

print(palindrome('abcba'))