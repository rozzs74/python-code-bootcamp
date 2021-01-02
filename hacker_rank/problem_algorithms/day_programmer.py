def get_programmer_day(y):
    if y == 1918:
        return f"26.09.{y}"
    elif y <= 1917:
        if y % 4 == 0:
            return f"12.09.{y}"
        else:
            return f"13.09.{y}"
    else:
        month = 0
        if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
            month = 12
        else:
            month = 13
        return f"{month}.09.{y}"

a = get_programmer_day(2700)
print(a)
