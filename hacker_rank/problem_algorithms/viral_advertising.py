# https://www.hackerrank.com/challenges/strange-advertising/problem?h_r=next-challenge&h_v=zen
def viralAdvertising(n):
    total = 2;
    liked = 2;
    for _ in range(n-1):
        liked = liked * 3//2
        total += liked
    return total
