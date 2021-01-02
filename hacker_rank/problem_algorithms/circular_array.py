# https://www.hackerrank.com/challenges/circular-array-rotation/problem
def circularArrayRotation(a, k, queries):
    FRONT = 0
    i = 0
    q = len(queries)
    for _ in range(k):
        i += 1
        a.insert(FRONT, a.pop())
        if i == k:
            j = 0
            items = []
            while q > 0:
                index = queries[j]
                el = a[index]
                items.append(el)
                j += 1 
                if j == q:
                    return items

# a = circularArrayRotation([3, 4, 5], 2, [1, 2])
a = circularArrayRotation([1,2,3], 2, [0, 1, 2])

print(' '.join(map(str, a)))
