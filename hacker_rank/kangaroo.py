#https://www.hackerrank.com/challenges/kangaroo/problem?h_r=next-challenge&h_v=zen


def kangaroo(x1, v1, x2, v2):
    print(f"x1 {x1}")
    print(f"v1 {v1}")
    print(f"x2 {x2}")
    print(f"v2 {v2}")
    k1_jump_result = x1 + v1
    k2_jump_result = x2 + v2
    
    print(f"k1_jump_result {k1_jump_result}")
    print(f"k2_jump_result {k2_jump_result}")
    return 1



result = kangaroo(0, 3, 4, 2)
