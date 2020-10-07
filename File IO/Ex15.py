# Write a Python program to read a random line from a file. 

import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    print(lines)
    return random.choice(lines)

print(random_line('notest.txt'))