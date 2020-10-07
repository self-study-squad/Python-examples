#Write a Python program to reverse words in a string.

import textwrap

def revstr(strip):
    for line in strip.split('\n'):
        return(' '.join(line.split()[::-1]))

stringip = input('Input a string: ')
stringop = revstr(stringip)
print('String after process: %s'%stringop)