# Write a Python program to issubset and issuperset.

setx = set(['apple','mango'])
sety = set(['mango','orange'])
setz = set(['mango'])

issubset = setx <= sety
print(issubset)

issuperset = setx >= sety
print(issuperset)

issubset = setz <= sety
print(issubset)

issuperset = setz >= sety
print(issuperset)
