#Write a Python program to count the number of characters (character frequency) in a string.

def sol(string):
    dict = {}
    for n in string:
        keys = dict.keys()
        if n in keys: 
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

ip_string = input('Input the string: ')
print('The number of each character in this string is: ')
print(sol(ip_string))