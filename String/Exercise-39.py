#Write a Python program to reverse a string. 

def revstr(strip):
    result = ''.join(reversed(strip))
    return result

stringip = input('Input a string: ')
stringop = revstr(stringip)
print('String after reversed: %s'%stringop)