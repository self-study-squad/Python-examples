# Write a Python program to convert an array to an ordinary list with the same items.


from array import *
arrip = array('i',[1,3,5,3,7,1,9,3])
num_list = arrip.tolist()
print(num_list)