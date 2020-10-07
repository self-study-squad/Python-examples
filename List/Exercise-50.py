# Write a Python program to sort a list of nested dictionaries.

my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]

my_list.sort(key= lambda e: e['key']['subkey'], reverse= True)
print(my_list)