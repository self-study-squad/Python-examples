# Write a Python program to get the frequency of the elements in a list.

my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]

import collections
freq = collections.Counter(my_list)
print(freq)
