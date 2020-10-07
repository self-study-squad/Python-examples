#Write a Python program to check whether a string starts with specified characters.

stringip = input('Input a string: ')
firstChars = input('Input first characters to check: ')

if stringip.startswith(firstChars):
    print('Result : True')
else:
    print('Result : False')