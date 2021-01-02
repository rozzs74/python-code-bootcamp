
#https://www.hackerrank.com/challenges/drawing-book/problem?h_r=next-challenge&h_v=zen
def pageCount(n, p):
    return min(p//2, n//2- p//2)