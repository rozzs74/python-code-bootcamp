# Description: Program that creats triangle
#  Return n copies of the front;
# Author: John Royce Punay
# Date created: March 11, 2018 7:04 AM
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
# ***********
# ************
# *************
# **************
# ***************
# ****************
# *****************
# ******************
# *******************
# ********************


def create_triangle(lower, upper):
    for i in range(lower, upper):
        print("*" * (i + 1))


create_triangle(1,20)