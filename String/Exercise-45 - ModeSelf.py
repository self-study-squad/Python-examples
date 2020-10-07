#Write a Python program to check if a string contains all letters of the alphabet.

import string
alphabet = set(string.ascii_lowercase)
strip = 'The quick brown fox jumps over the lazy dog'
print(set(strip.lower()) >= alphabet)
strip ='The quick brown fox jumps over the lazy cat'
print(set(strip.lower()) >= alphabet)
