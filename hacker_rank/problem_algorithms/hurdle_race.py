# https://www.hackerrank.com/challenges/the-hurdle-race/problem
#https://en.wikipedia.org/wiki/Hurdling

def hurdleRace(k, heights):
    heights_length = len(heights)
    tallest_height = max(list(set(heights)))
    dose = 0
    if k > tallest_height:
        return dose
    else:
        return tallest_height - k
# 0
# a = hurdleRace(7, [2, 5, 4, 5, 2])
# a = hurdleRace(4, [1, 6, 3, 5, 2])
a = hurdleRace(1, [1,2,3,3,2])
print(f"final answer {a}")

 # remove dups
# get the highest number
# subtract highest number to unit