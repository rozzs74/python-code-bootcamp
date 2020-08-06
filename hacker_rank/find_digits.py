
# https://www.hackerrank.com/challenges/find-digits/problem
def findDigits(divisor):
    integers = str(divisor)
    count = 0
    for integer in integers:
        dividend = int(integer)
        if dividend != 0 and divisor % dividend == 0:
            count += 1
    return count
# a = findDigits(12)
# print(a)
a = findDigits(1012)
print(a)