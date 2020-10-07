# Write a Python program to get the maximum and minimum value in a dictionary.

my_dict = {'x' : 200, 'y' : 5874,'z' : 560}

max_dict = max(my_dict.keys(),key= lambda k: my_dict[k])
min_dict = min(my_dict.keys(),key= lambda k: my_dict[k])

print('Max value: ',my_dict[max_dict])
print('Min value: ',my_dict[min_dict])