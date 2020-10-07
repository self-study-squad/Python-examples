# Write a Python program to create a list with infinite elements.

import itertools

c = itertools.count()
for i in range(10):
    print(next(c))
print(c)
next(c)
print(c)