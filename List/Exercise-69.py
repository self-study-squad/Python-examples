# Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

import itertools

listip = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
listip.sort()

listop = list(num for num,_ in itertools.groupby(listip))

print(listop)