# Write a Python program to convert a list of tuples into a dictionary.

# create a list
l = [('x', 1), ('x', 2), ('x', 3), ('y', 1), ('y', 2), ('y', 1)]
d = dict()
for a,b in l:
    d.setdefault(a,[]).append(b)

print(d)