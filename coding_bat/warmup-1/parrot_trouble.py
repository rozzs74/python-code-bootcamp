# Description: We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
# Author: John Royce Punay
# Date created: March 4, 2018 7:02 PM
# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False

# Solution 1
def parrot_trouble(is_parrot_talking, hour_time):
    if (hour_time < 7 or hour_time > 20) and is_parrot_talking:
        return True
    else:
        return False

# Solution 2

def parrot_trouble2(is_parrot_talking, hour_time):
    return (is_parrot_talking and (hour_time < 7 or hour_time > 20))
    
print(parrot_trouble(True, 7))