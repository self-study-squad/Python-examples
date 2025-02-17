# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

from collections import Counter, defaultdict

strip = 'w3resource'

my_dict = {}
for letter in strip:
    my_dict[letter] = my_dict.get(letter,0) + 1
print(my_dict)