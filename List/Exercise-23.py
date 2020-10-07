# Write a Python program to flatten a shallow list.

original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]

import itertools

newlist = list(itertools.chain(*original_list))
print(newlist)