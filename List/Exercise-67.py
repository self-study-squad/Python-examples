# Write a Python program to find all the values in a list are greater than a specified number. 

list1 = [220, 330, 500]
list2 = [12, 17, 21]

print(all(x >= 200 for x in list1))
print(all(x > 17 for x in list2))