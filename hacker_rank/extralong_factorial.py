# https://www.hackerrank.com/challenges/extra-long-factorials/problem?h_r=next-challenge&h_v=zen
def extraLongFactorials(n):
    i = n
    for q in range(1, n):
        i *= (n - q)
    return print(i)



a = extraLongFactorials(30)
print(a)
