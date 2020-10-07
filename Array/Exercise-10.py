# Write a Python program to insert a new item before the second element in an existing array.

from array import *
arr = array('i',[1,3,5,7,9])
arr.insert(1,4)
print(arr)