from math import sqrt

# # Solution 1 easy and simple beginner level 
# def is_prime_or_composite_number(number):
#     # Prime numbers are those not factorable
#     # Composite are factorable
#     for n in range(2, number):
#         if number % n == 0:
#             print("It's composite number {}".format(number))
#             break
#     else:
#         print("It's prime number {}".format(number))


# Solution 2 hard and better expert level

def is_prime_or_composite_number2(number):
    if number % 2 == 0 and number > 2:
        return False
    for i in range(3, int(sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

print(is_prime_or_composite_number2(1))