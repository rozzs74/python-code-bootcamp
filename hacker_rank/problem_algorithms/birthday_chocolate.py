 # https://www.hackerrank.com/challenges/the-birthday-bar/problem



def birthdays(s, d, m):
    squares_length = len(s)

    if 1 <= squares_length and squares_length <= 100:
        print(f"s {s}")
        print(f"sl {squares_length}")
        print(f"d {d}")
        print(f"m {m}")
        i = 0
        count = 0
        t = 0
        while 0 < squares_length:
            el = s[i:m]
            m = m + 1
            el_length = len(el)
            if sum(el) == d:
                count += 1
            i += 1
            if i == squares_length:
                #print(f"count {count}")
                break
    return count


result = birthdays([1, 1, 1, 1, 1, 1,], 3, 2)
#result = birthdays([4], 4, 1)

#result = birthdays([1, 2, 1, 3, 2], 3, 2)
#result = birthdays([2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1], 18, 7)
#print(result)
