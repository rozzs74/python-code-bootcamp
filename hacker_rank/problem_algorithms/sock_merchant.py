# https://www.hackerrank.com/challenges/sock-merchant/problem
# https://www.thepoorcoder.com/hackerrank-sock-merchant-solution/

from collections import Counter

def sockMerchant(n, arr):
    items = Counter(arr)
    to_search = 2
    total = []
    for item in items.values():
        pair = item // to_search
        if pair:
            total.append(pair)
    return sum(total)

    
a = sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])       
print(a)