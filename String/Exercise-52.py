#Write a Python program to print all permutations with given repetition number of characters of a given string.

from itertools import product

def all_rep(strip,repno):
    result = []
    chars = list(strip)
    for c in product(chars,repeat = repno):
        result.append(c)
    return result



print(all_rep('w3resource.com', 2))
print(all_rep('w3resource.com',3))
