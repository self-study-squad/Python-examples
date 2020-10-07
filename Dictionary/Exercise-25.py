# Write a Python program to print a dictionary in table format.

tbdic = {'c1': [1,2,3], 'c2': [5,6,7], 'c3':[9,10,11]}

for row in zip(*([key] + (value) for key, value in sorted(tbdic.items()))):
    print(*row)