#  Write a Python program to get the array size of types unsigned integer and float. 
# Expected Output:
# 4 
# 4

from array import array
a = array('i', (12,25))
print(a.itemsize)
a = array('f',(12.236,36.36))
print(a.itemsize)
