def cutTheSticks(arr):
    results=[]
    while len(arr)>=1:
        results.append(len(arr))
        minlen=min(arr)
        arr=[i for i in arr if i>minlen]
    return results

a = cutTheSticks([5, 4, 4, 2, 2, 8])
# https://www.hackerrank.com/challenges/cut-the-sticks/problem
# 5 4 4 2 2 8  

# 2 - 8 = 6 *
# 2 -2 = 0
# 2-2- = 0
# 2-4 = 2
# 2-4 = 2
# 2-5 = 3


# 6 2 2 3
# 2 - 6 = 4 *
# 2-2 = 0
# 2-2 =0
# 2-3 1

# 4 1
# 1 - 4  = 3   2 *
# 1 -1 = 0
#  3  0 

#  0 - 1 1