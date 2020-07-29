# https://www.hackerrank.com/challenges/utopian-tree/problem

def utopianTree(growth_cycles):
    growth_length = len(growth_cycles) - 1
    growth_cycles.pop(0)
    test_case = growth_cycles[0]
    i = 0
    # while growth_length > 1:
    #     el = growth_cycles[i]
    #     print(el)

    #     i += 1
    #     if i == growth_length:
    #         break

    t = 0
    for n in range(0, 61):
        if n > 2:
            if n % 2 != 0:
                print(f"o={n}")
                t = n * 2
            else:
                print(f"e={n}")
                t = t + 1
            # print(t, i, n)

        i += 1


    # + 1
    # x 2



a = utopianTree([3, 0 ,1, 4])