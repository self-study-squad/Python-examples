#  Write a Python program to create the colon of a tuple.

import copy

tuplex = ("hll",5,[],True)
print(tuplex)

# make a copy of a tuple using deepcopy() function

tuple_clone = copy.deepcopy(tuplex)
print(tuple_clone)
tuple_clone[2].append(50)
print(tuple_clone)

tuplex[2].append(250)
print(tuplex)

antuplex = tuplex
print(antuplex)

atuplex = copy.deepcopy(tuplex)
atuplex[2].append([3,5])
print(atuplex)
print(id(atuplex))
print(tuplex)
print(id(tuplex))