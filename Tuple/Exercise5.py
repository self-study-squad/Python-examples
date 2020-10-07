#  Write a Python program to add an item in a tuple.

tupip = 2, 3, 5
print(tupip)

tupip = tupip + (9,)
print(tupip)

tupip += (15,)
print(tupip)

tupip = tupip[:3] + (12,19,25) + tupip[:5]
print(tupip)

listx = list(tupip)
listx.append(90)
print(listx)
tupop = tuple(listx)
print(tupop)
