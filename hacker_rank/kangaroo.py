#https://www.hackerrank.com/challenges/kangaroo/problem?h_r=next-challenge&h_v=zen


def kangaroo(x1, v1, x2, v2):
    k1_jump_result = x1
    k2_jump_result = x2
    i = 0
    if x2 > x1 or v2 > v1:
        return "NO"
    else :
        while True:
            x1 = x1 + v1
            x2 = x2 + v2
            i += 1
            if x1 == x2:
                return "YES"


# result = kangaroo(0, 3, 4, 2)
# result = kangaroo(2, 1, 1, 2)
# result = kangaroo(0, 2, 5, 3)
result = kangaroo(21, 6, 47, 3)

# 21 6 47 3
print(result)
# 0 2 5 3


