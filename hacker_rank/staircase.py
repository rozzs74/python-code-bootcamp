def staircase(n):
    for item in range (1, n + 1):
        a = "#"
        print(n)
        print("{}".format(a * item).rjust(n))
    return 1
n = staircase(6)
