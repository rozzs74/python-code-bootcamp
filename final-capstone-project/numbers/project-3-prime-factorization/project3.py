"""
Have the user enter a number and find all Prime Factors (if there are any) and display them.
"""

def get_user_number():
    while True:
        try:
            number = int(input("Please enter number you to get prime factors: "))
        except ValueError:
            print("Invalid number")
            continue
        else:
            # print(check_number_if_even(number))
            check_number_if_even(number)
            break

def check_number_if_even(number):

    primefac = []

    d = 2

    while d * d <= number:
        while number % d == 0:
            primefac.append(d)
            number //= d
        d += 1
    if number > 1:
        primefac.append(number)
    return primefac


if __name__ == "__main__":
    get_user_number()