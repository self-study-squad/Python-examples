# Write a Python program to convert a list of multiple integers into a single integer.

L = [11, 33, 50]
x = int("".join(map(str,L)))
print(x)