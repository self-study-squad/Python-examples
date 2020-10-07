# Write a Python program to convert a list into a nested dictionary of keys.

num_list = [1, 2, 3, 4]
opdic = current = {}

for name in num_list:
    current[name] = {}
    current = current[name]

print(opdic)