# Write a Python program to create an array contains six integers. 
# Also print all the members of the array.
# Expected Output:
# 10
# 20
# 30
# 40
# 50

from array import array
my_array = array('i',[10,20,30,40,50])
for i in my_array: 
    print(i)