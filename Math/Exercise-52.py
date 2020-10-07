# Write a Python program to shuffle the following elements randomly.
# Sample elements : [1, 2, 3, 4, 5, 6, 7]
# Expected Output :
# [2, 1, 7, 5, 3, 4, 6]

import random

nums = [2, 1, 7, 5, 3, 4, 6]
random.shuffle(nums)
print(nums)