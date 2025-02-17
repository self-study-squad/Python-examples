# Write a Python program to create an instance of an OrderedDict using a given dictionary. 
# Sort the dictionary during the creation and print the members of the dictionary in reverse 
# order.
# Expected Output: 
# Angola 244
# Andorra 376
# Algeria 213
# Afghanistan 93
# Albania 355
# In reverse order:
# Albania 355
# Afghanistan 93
# Algeria 213
# Andorra 376
# Angola 244

from collections import OrderedDict
dict = {'Afghanistan': 93, 'Albania': 355, 'Algeria': 213, 'Andorra': 376, 'Angola': 244}
new_dict = OrderedDict(dict.items())
for key in new_dict:
    print(key, new_dict[key])
    
print('\nIn reverse order: ')
for key in reversed(new_dict):
    print(key, new_dict[key])
