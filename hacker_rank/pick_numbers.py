#https://www.hackerrank.com/challenges/picking-numbers/problem?h_r=next-challenge&h_v=zen
# https://www.w3schools.com/python/ref_list_count.asp
# https://www.programiz.com/python-programming/methods/list/count
# list.count() simply return how many times the element repeat in the list.
def pickingNumbers(arr):
    total = 0
    i = 0
    arr_length = len(arr)
    while arr_length > 1:
        el = arr[i]
        a = arr.count(el)
        b = arr.count(el + 1)
        total = max(total, a + b)
        i += 1
        if i == arr_length:
            return total


# a = pickingNumbers([1, 1, 2, 2, 4, 4, 5, 5, 5]
# a = pickingNumbers([1, 2, 2, 3, 1, 2])
a = pickingNumbers([4, 6, 5, 3, 3, 1]) 
#3