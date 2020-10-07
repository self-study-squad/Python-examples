# Write a Python program to find common items from two lists.

color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"

listop = set(color1) & set(color2)
print(listop)