# Write a Python program to create an array of 5 integers and display the array items. 
# Access individual element through indexes.

from array import *
array_num = array('i',[1,3,5,7,9])
for i in array_num:
    print(i)

print('Access first three items individually')
print(array_num[0])
print(array_num[1])
print(array_num[2])

for j in array_num:
    print(j)
    
# arr = array('i',[10,8,6,4,2])
# print(arr)