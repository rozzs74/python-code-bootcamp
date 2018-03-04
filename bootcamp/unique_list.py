# Description: Program that return unique lists
# Author: John Royce Punay
# Date created: March 3, 2018 11:39 AM



mylists = [1,1,1,1,2,2,2,2,3,3,3,3,4]

# solution 1
print(list(set(mylists)))

# solution 2
def unique_list(list):
    new_list = []
    for item in list:
        if item not in new_list:
            new_list.append(item)

    return new_list
print(unique_list(mylists))