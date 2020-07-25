def getMoneySpent(keyboards, drives, total_money):
    k_length = len(keyboards)
    i = 0
    within_range = []
    too_much = True
    while k_length >= 0:
        total = 0
        keyboard_price = keyboards[i]
        for drive in drives:
            total = keyboard_price + drive
            if total <= total_money:
                within_range.append(total)
                too_much = False
        i += 1
        if i == k_length:
            return max(within_range) if too_much != True else -1
a = getMoneySpent([40, 50, 60], [5, 8, 12], 60)

# a = getMoneySpent([3, 1], [5, 2, 8], 10)
# a = getMoneySpent([4], [5], 5)
print(a)
# 9