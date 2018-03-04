# #LESSER OF TWO EVENS:
# Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
#     lesser_of_two_evens(2,4) --> 2
#     lesser_of_two_evens(2,5) --> 5


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Begginer way
# def lesser_of_two_evens(x, y):
#     # Check if two parameters are even (1)
#     if is_even(x) and is_even(y):
#         if x > y:
#             return y
#         else:
#             return x
#     else:   
#         if x > y:
#             return x
#         else:
#             return y


# Knowledgeable way
def lesser_of_two_evens(x, y):
    if is_even(x) and is_even(y):
        return min(x,y)
    else:
        return max(x,y)

result = lesser_of_two_evens(100000,1)
print(result)