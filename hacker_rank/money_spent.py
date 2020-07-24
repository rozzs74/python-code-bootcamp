def getMoneySpent(keyboards, drives, total_money):
    k_length = len(keyboards)
    d_length = len(drives)
    i = 0
    while k_length > 1:
        keyboard_price = keyboards[i]
        drive_price = drives[i]
        total = keyboard_price + drive_price
        if total < total_money:
            print(total)
        i += 1
        if i == k_length:
            break
    pass

a = getMoneySpent([40, 50, 60], [5, 8, 12], 60)

# 9