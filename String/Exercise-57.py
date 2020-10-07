#Write a Python program to remove spaces from a given string.

def rmsp(strip):
    result = strip.replace(' ','')
    return result

stringip = input('Input as tring: ')
print(rmsp(stringip))