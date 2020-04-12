
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_length = len(apples)
    oranges_length = len(oranges)
    i = 0
    apple_distance = []
    orange_distance = []
    while apple_length >= 1:
        apple = apples[i] + a
        if apple >= s and apple <= t:
            apple_distance.append(apple)
        i = i + 1
        if apple_length == i:
            i = 0
            while oranges_length >= 1:
                orange = oranges[i] + b
                if orange >= s and orange <= t:
                    orange_distance.append(orange)
                i += 1
                if oranges_length == i:
                    print(f"{len(apple_distance)}")
                    print(f"{len(orange_distance)}")
                    break
            break
    return


# result = countApplesAndOranges(7, 10, 4, 12, [2, 3, -4], [3, -2, -4])
result = countApplesAndOranges(2, 3, 1, 5, [2], [-2])

# 2 3
# 1 5
# 1 1
# 2
# -2 
# 11


# 2 3
# 1 5
# 1 1
# -2
# -1

# 00
