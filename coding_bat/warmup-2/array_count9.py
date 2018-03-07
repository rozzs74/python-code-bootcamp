# Description: Given an array of ints, return the number of 9's in the array.
# Author: John Royce Punay
# Date created: March 7, 2018 7:36 PM
# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3


# Solution 1
def array_count91(items):
    return len([item for item in items if item == 9])


print(array_count91([1, 9, 9, 3, 9]))

# Solution 2
def array_count92(nums):
  count = 0
  # Standard loop to look at each value
  for num in nums:
    if num == 9:
      count = count + 1

  return count