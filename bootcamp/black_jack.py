# BLACKJACK: 
# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19


# My solution
def blackjack(x, y, z):
    if x in range(1, 12) and y in range(1, 12) and z in range(1, 12):
        sum = x + y + z
        if sum <= 21:
            return sum
        elif sum > 21 and (x == 11 or y == 11 or z ==11):
            return sum - 10
        else:
            return "BUST"
    else:
        print("Oops")        
        return False

# Portilla solution
# def blackjack(a,b,c):
    
#     if sum((a,b,c)) <= 21:
#         return sum((a,b,c))
#     elif sum((a,b,c)) <=31 and 11 in (a,b,c):
#         return sum((a,b,c)) - 10
#     else:
#         return 'BUST'

print(blackjack(5,6,7))