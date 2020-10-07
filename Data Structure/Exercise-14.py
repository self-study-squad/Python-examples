# Write a Python program to get an array buffer information.
# Expected Output:
# Array buffer start address in memory and number of elements.
# (25855056, 2)

from array import array
a = array('i',(12,25))
print('Array buffer start address in memory and number of elements.')
print(a.buffer_info())