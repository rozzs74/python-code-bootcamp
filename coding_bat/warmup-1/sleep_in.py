# Description: Program that can determine if you can sleep in weekday and vacation
# Author: John Royce Punay
# Date created: March 4, 2018 12:30 PM


# my solution 
def sleep_in_1(weekday, vacation):
    if weekday and not vacation:
        return False
    elif vacation and not weekday:
        return True
    else: 
        return False

# short solution
def sleep_in_2(weekday, vacation):
    return not weekday or vacation

print(sleep_in_2(False, True))