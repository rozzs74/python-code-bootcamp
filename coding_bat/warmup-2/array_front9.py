# Description: Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
# The array length may be less than 4.
# Author: John Royce Punay
# Date created: March 7, 2018 7:57 PM
# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False


def array_front9(nums):     
  end = len(nums)
  if end > 4:
    end = 4
  
  for i in range(end):
    if nums[i] == 9:
      return True
  return False

print(array_front9([1, 2, 1, 3, 4]))