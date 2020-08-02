# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?h_r=next-challenge&h_v=zen
def beautifulDays(start, end, divisor):
    count = 0
    for i in range(start, end+1):
        final = 0
        num = str(i)
        reversed_int  = int(num[::-1])
        numerator = abs(i - reversed_int)
        final = numerator // divisor
        if numerator % divisor == 0:
            count += 1
    return count
a = beautifulDays(1, 2000000, 23047885)
print(a)
# a = beautifulDays(123, 456789, 189)
#2


