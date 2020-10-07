#Write a Python program to check whether a string starts with specified characters.
def ck(strip,chrip):
    if strip.find(chrip) == 0:
        return True
    return False


stringip = input('Input a string: ')
firstChars = input('Input first characters to check: ')

if ck(stringip, firstChars):
    print('Result: True')
else:
    print('Result: False')