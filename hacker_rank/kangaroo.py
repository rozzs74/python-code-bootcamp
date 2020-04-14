#https://www.hackerrank.com/challenges/kangaroo/problem?h_r=next-challenge&h_v=zen


def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 > v1: 
        return "NO"
    i = 0
    while 1 < 10000:
        x1 = x1 + v1
        # print(f"x1 {x1}")
        x2 = x2 + v2
        i += 1
        if x1 == x2:
            return "YES"
        if i == 10000 and x1 != x2:
            return "NO"
    return "NO"
# result = kangaroo(0, 3, 4, 2)
# result = kangaroo(2, 1, 1, 2)
result = kangaroo(0, 2, 5, 3)
# result = kangaroo(21, 6, 47, 3) # NO

# result = kangaroo(0, 3, 4,2)
# 21 6 47 3
print(result)
# 0 2 5 3


