# Write a Python program to remove an item from a tuple.

tuplex = 'w',3,'r','e','s','o','u','r','s','e'
n1tuple = tuplex[:2] + tuplex[3:]
print(n1tuple)

listx = list(tuplex)
listx.remove('r')
print(listx)
n2tuple = tuple(listx)
print(n2tuple)