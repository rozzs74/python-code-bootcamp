# Description: Program that handle exception thrown by the code below using try and except blocks
# Author: John Royce Punay
# Date created: March 11, 2018 8:09 AM

try:
    for i in ['a', 'b', 'c']:
        print(1**2)
except TypeError:
    print("Invalid operation")