#Write a Python program to remove duplicate characters of a given string.

from collections import OrderedDict

def rmlp(strip):
    return ''.join(OrderedDict.fromkeys(strip))

print(rmlp("python exercises practice solution"))
print(rmlp("w3resource"))
