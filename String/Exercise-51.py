#Write a Python program to find the first non-repeating character in given string.

import string

def check(strip):
    ck = True
    for i in strip: 
        if strip.count(i) == 1:
            print('%s'%i)
            ck = False
            break
    if ck:
        print('None')
        
stringip1 = 'abcdef'
stringip2 = 'abcabcdef'
stringip3 = 'aabbcc'

check(stringip1)
check(stringip2)
check(stringip3)
