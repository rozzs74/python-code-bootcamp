# https://www.hackerrank.com/challenges/sock-merchant/problem
# https://www.thepoorcoder.com/hackerrank-sock-merchant-solution/

from collections import Counter

def sockMerchant(n, arr):
    items = Counter(arr)
    to_search = 2
    return sum(item//to_search for item in items.values())

# search 
# remove
a = sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])       
print(a)