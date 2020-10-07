#Write a Python program to sort a string lexicographically.

def sortstr(strip):
    result = sorted(sorted(strip))
    return result

stringip = input('Input a string: ')
print('String after sorted: %s'%sortstr(stringip))