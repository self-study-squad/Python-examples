# Write a Python program to find the first repeated character in a given string.

def fd(strip):
    result = True
    for i in strip: 
        if strip.count(i) != 1: 
            result = i
            break
    return result

stringip = input('Input a string: ')
if fd(stringip)  == True:
    print('None are repeated!')
else:
    print('First repeated char: %s'%fd(stringip))