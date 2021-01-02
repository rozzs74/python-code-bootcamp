# https://www.hackerrank.com/challenges/counting-valleys/problem
# https://stackoverflow.com/questions/55777078/counting-valleys-question-from-hacker-rank
# U + 1
# D  - 1
# Diff = 0 that is a valley

def countingValleys(no_steps, paths):
    count = 0
    total_valley = 0
    for index in range(0, len(paths)):
        item = paths[index]
        if item == "U":
            count += 1
            if count == 0:
                total_valley += 1
        else:
            count -= 1
    return total_valley

a = countingValleys(8, "UDDDUDUU")
print(a)