#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

def sol(string):
    if len(string) >2:
        result = string[:2]+string[-2:]
    else:
        result = 'Empty String'
    return result
input_str = input('Input a string: ')
print('String after solving: %s'%(sol(input_str)))