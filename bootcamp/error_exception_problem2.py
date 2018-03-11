# Description: Program that handle exception thrown by the code below using try and except blocks. Then use a finally block to print
# 'All done'
# Author: John Royce Punay
# Date created: March 11, 2018 8:15 AM

try:
    x = 5
    y = 0
    z = x / y
except: 
    ZeroDivisionError
    print("Division undefined")
finally:
    print("All done")