# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output: 
# ac
# ad
# bc
# bd

import itertools

d = {'1':['a','b'], '2':['c','d']}

for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
                               print(''.join(combo))